import os
from unittest.mock import MagicMock

import pytest
from dotenv import load_dotenv

from financial_datasets.dataset import Dataset, DatasetItem
from financial_datasets.generator import DatasetGenerator

# Load the environment variables from .env file
load_dotenv()


def test_create_generator() -> None:
    def create_openai_generator() -> DatasetGenerator:
        return DatasetGenerator(
            model="gpt-3.5-turbo-0125",
            api_key="fake_key"
        )

    def create_anthropic_generator() -> DatasetGenerator:
        return DatasetGenerator(
            model="claude-3-haiku-20240307",
            api_key="fake_key"
        )

    # Creating OpenAI generator should not raise an exception
    openai_generator = create_openai_generator()
    assert openai_generator is not None

    # Creating Anthropic generator should raise an exception
    with pytest.raises(NotImplementedError):
        create_anthropic_generator()


def test_generate_from_texts() -> None:
    def create_openai_generator() -> DatasetGenerator:
        return DatasetGenerator(
            model="gpt-3.5-turbo-0125",
            api_key=os.environ.get('OPENAI_API_KEY')
        )

    # Create OpenAI generator
    generator = create_openai_generator()

    # Define some texts from a 10-K
    texts = [
        "Our business depends on Hosts maintaining their listings on our platform and engaging in practices that encourage guests to book those listings, including increasing the number of nights and experiences that are available to book, providing timely responses to inquiries from guests, offering a variety of desirable and differentiated listings at competitive prices that meet the expectations of guests, and offering exceptional hospitality, services, and experiences to guests",
        "In 2023, revenue increased by 18% to $9.9 billion compared to 2022, primarily due to a 14% increase in Nights and Experiences Booked of 54.5 million combined with higher average daily rates driving a 16% increase in Gross Booking Value of $10.0 billion. The growth in revenue demonstrated continued strong travel demand. On a constant-currency basis, revenue increased 17% in 2023 compared to 2022."
    ]

    # Generate questions
    dataset = generator.generate_from_texts(texts=texts, max_questions=10)
    items = dataset.items
    assert len(items) <= 10


def test_generate_from_texts_with_mock():
    # Create a mock response
    mock_response = Dataset(
        items=[
            DatasetItem(question="Question 1", answer="Answer 1", context="Context 1"),
            DatasetItem(question="Question 2", answer="Answer 2", context="Context 2"),
        ]
    )

    # Create a mock OpenAI client
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = mock_response

    # Create a DatasetGenerator instance with the mock client
    dataset_generator = DatasetGenerator(model="gpt-3.5-turbo", api_key="mock_api_key")
    dataset_generator._client = mock_client

    # Define the input texts and max_questions
    texts = ["Text 1", "Text 2", "Text 3"]
    max_questions = 6

    # Call the generate_from_texts method
    dataset = dataset_generator.generate_from_texts(texts, max_questions)

    # Assert the length of items generated
    assert len(dataset.items) == max_questions

    # Assert the number of times the OpenAI client's create method was called
    assert mock_client.chat.completions.create.call_count <= len(texts)


def test_generate_from_10K():
    def create_openai_generator() -> DatasetGenerator:
        return DatasetGenerator(
            model="gpt-3.5-turbo-0125",
            api_key=os.environ.get('OPENAI_API_KEY')
        )

    # Create OpenAI generator
    generator = create_openai_generator()

    # Generate questions from the SEC filing
    dataset = generator.generate_from_10K(
        ticker="TSLA",
        year=2023,
        max_questions=10,
    )
    items = dataset.items
    assert len(items) <= 10


def test_generate_from_10Q():
    def create_openai_generator() -> DatasetGenerator:
        return DatasetGenerator(
            model="gpt-3.5-turbo-0125",
            api_key=os.environ.get('OPENAI_API_KEY')
        )

    # Create OpenAI generator
    generator = create_openai_generator()

    # Generate questions from Costco's 2024 Q1 10-Q filing
    dataset = generator.generate_from_10Q(
        ticker="COST",
        year=2024,
        quarter=1,
        max_questions=10,
    )

    items = dataset.items
    assert len(items) <= 10


def test_generate_from_pdf():
    def create_openai_generator() -> DatasetGenerator:
        return DatasetGenerator(
            model="gpt-3.5-turbo-0125",
            api_key=os.environ.get('OPENAI_API_KEY')
        )

    # Create OpenAI generator
    generator = create_openai_generator()

    # Generate questions from Berkshire's 2023 letter
    dataset = generator.generate_from_pdf(
        url="https://www.berkshirehathaway.com/letters/2023ltr.pdf",
        max_questions=10,
    )
    items = dataset.items
    assert len(items) <= 10
