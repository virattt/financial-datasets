import re
from typing import List

from edgar import Company, set_identity, get_filings

from financial_datasets.filings import filter_filings, FilingItem

default_sec_identity = "gary gary@financialdatasets.org"

valid_item_names = set([item.value for item in FilingItem])


class FilingParser:

    def get_10K_items(
        self,
        ticker: str,
        year: int,
        item_names: List[str] = [],
        sec_identity=default_sec_identity,
    ) -> List[str]:
        """
        Get the items from a 10-K filing for a given company and year.

        :param ticker: The stock ticker symbol.
        :param year: The year of the filing.
        :param item_names: List of Items to retrieve from the 10-K.
        :param sec_identity: The identity to use when making requests to the SEC API.

        :return: A list of items from the 10-K filing.
        """

        # Ensure item_names are valid
        if any(item_name not in valid_item_names for item_name in item_names):
            raise ValueError(f"Item names may only be one of {sorted(valid_item_names)}.")

        # Tell the SEC who is making the request
        set_identity(sec_identity)

        if not ticker:
            raise ValueError("Ticker symbol is required.")

        if not year:
            raise ValueError("Year is required.")

        # Create a Company object
        company = Company(ticker)

        # Retrieve the SEC filing
        filings = company.get_filings(form="10-K")
        filing = filter_filings(filings, "10-K", year).obj()

        # Get the Item names in the filing
        filing_item_names = set([item_name for item_name in filing.items])

        # Figure out which Items to return
        items_to_return = [] if item_names else filing.items
        for item_name in item_names:
            if item_name in filing_item_names:
                items_to_return.append(item_name)

        # Get the items
        items = [filing[item] for item in items_to_return]

        # Remove any newline characters and trim outer whitespace
        items = [item.replace("\n", " ").strip() for item in items]

        # Remove any sequence of 3 or more '-' or '.' characters
        pattern1 = r'-{3,}|\.{3,}'
        items = [re.sub(pattern1, '', item) for item in items]

        # Remove any sequence of 2 or more '+' characters
        pattern2 = r'\+{2,}'
        items = [re.sub(pattern2, '', item) for item in items]

        return items

    def get_10Q_items(
        self,
        ticker: str,
        year: int,
        quarter: int,
        item_names: List[str] = [],
        sec_identity=default_sec_identity,
    ) -> List[str]:
        """
        Get the items from a 10-Q filing for a given company, year, and quarter.

        :param ticker: The stock ticker symbol.
        :param year: The year of the filing.
        :param quarter: The quarter of the filing.
        :param item_names: List of Items to retrieve from the 10-Q.
        :param sec_identity: The identity to use when making requests to the SEC API.

        :return: A list of items from the 10-Q filing.
        """

        # Ensure item_names are valid
        if any(item_name not in valid_item_names for item_name in item_names):
            raise ValueError(f"Item names may only be one of {sorted(valid_item_names)}.")

        # Tell the SEC who is making the request
        set_identity(sec_identity)

        if not ticker:
            raise ValueError("Ticker symbol is required.")

        if not year:
            raise ValueError("Year is required.")

        # Get all 10-Q filings for the given year and quarter
        filings = get_filings(year, quarter, form="10-Q")

        # Create a Company object
        company = Company(ticker)

        # Filter the filings to find the one for the company
        filing = next((f for f in filings if f.cik == company.cik), None)
        if not filing:
            raise ValueError(f"No 10-Q filing found for {ticker} in {year} Q{quarter}.")

        # Get the filing entities for the company
        company_filings = company.get_filings(accession_number=filing.accession_number)
        if not company_filings:
            raise ValueError(f"No 10-Q filing found for {ticker} in {year} Q{quarter}.")

        # Get the exact 10-Q filing for the company
        company_filing = company_filings[0].obj()

        # Get the Item names in the filing
        filing_item_names = set([item_name for item_name in company_filing.items])

        # Figure out which Items to return
        items_to_return = [] if item_names else company_filing.items
        for item_name in item_names:
            if item_name in filing_item_names:
                items_to_return.append(item_name)

        # Get the items
        items = [company_filing[item] for item in items_to_return]

        # Remove any newline characters and trim outer whitespace
        items = [item.replace("\n", " ").strip() for item in items]

        # Remove any sequence of 3 or more '-' or '.' characters
        pattern1 = r'-{3,}|\.{3,}'
        items = [re.sub(pattern1, '', item) for item in items]

        # Remove any sequence of 2 or more '+' characters
        pattern2 = r'\+{2,}'
        items = [re.sub(pattern2, '', item) for item in items]

        return items
