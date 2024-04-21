import re

from edgar import Company, set_identity, get_filings

from financial_datasets.filings import filter_filings


class FilingParser:

    def get_10K_items(
        self,
        ticker: str,
        year: int,
        sec_identity: str,
    ):
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
        items = [filing[item] for item in filing.items if len(filing[item]) > 200]  # Ignore short items like "Item 6. Reserved"

        # Remove any newline characters
        items = [item.replace("\n", " ") for item in items]

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
        sec_identity: str,
    ):
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
        company_filings = company.get_filings(form="10-Q", filing_date=filing.filing_date)
        if not company_filings:
            raise ValueError(f"No 10-Q filing found for {ticker} in {year} Q{quarter}.")

        # Get the exact 10-Q filing for the company
        company_filing = company_filings[0].obj()

        # Extract the items from the filing
        items = [company_filing[item] for item in company_filing.items if len(company_filing[item]) > 200]  # Ignore short items like "Item 6. Reserved"

        # Remove any newline characters
        items = [item.replace("\n", " ") for item in items]

        # Remove any sequence of 3 or more '-' or '.' characters
        pattern1 = r'-{3,}|\.{3,}'
        items = [re.sub(pattern1, '', item) for item in items]

        # Remove any sequence of 2 or more '+' characters
        pattern2 = r'\+{2,}'
        items = [re.sub(pattern2, '', item) for item in items]

        return items
