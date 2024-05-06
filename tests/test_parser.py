from financial_datasets.parser import FilingParser


def test_get_10K_items():
    # Given
    parser = FilingParser()

    # When
    items = parser.get_10K_items(
        ticker="SNOW",
        year=2023,
    )

    # Then
    assert len(items) > 0
    assert items[0].startswith("ITEM 1.")


def test_get_10K_items_with_items_param():
    # Given
    parser = FilingParser()

    # When
    items = parser.get_10K_items(
        ticker="SNOW",
        year=2023,
        item_names=["Item 1A", "Item 2"],
    )

    # Then
    assert len(items) == 2
    assert items[0].startswith("ITEM 1A")
    assert items[1].startswith("ITEM 2")


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
    assert items[0].startswith("ITEM 1")


def test_get_10Q_items_with_items_param():
    # Given
    parser = FilingParser()

    # When
    items = parser.get_10Q_items(
        ticker="SNOW",
        year=2023,
        quarter=2,
        item_names=["Item 1A", "Item 2"],
    )

    # Then
    assert len(items) == 2
    assert items[0].startswith("ITEM 1A")
    assert items[1].startswith("ITEM 2")
