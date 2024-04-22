from financial_datasets.parser import FilingParser


def test_get_10K_items():
    # Given
    parser = FilingParser()

    # When
    items = parser.get_10K_items(
        ticker="TSLA",
        year=2023,
    )

    # Then
    assert len(items) > 0
    assert items[0].startswith("ITEM 1.")


def test_get_10Q_items():
    # Given
    parser = FilingParser()

    # When
    items = parser.get_10Q_items(
        ticker="TSLA",
        year=2023,
        quarter=4,
    )

    # Then
    assert len(items) > 0
    assert items[0].startswith("ITEM 1.")
