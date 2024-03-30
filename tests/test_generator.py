import pytest

from financial_datasets.generator import DatasetGenerator
from financial_datasets.model import ModelConfig, ModelProvider


def test_create_generator() -> None:
    def create_openai_generator() -> DatasetGenerator:
        return DatasetGenerator(
            model_config=ModelConfig(
                provider=ModelProvider.OPEN_AI,
                name="gpt-3.5-turbo-0125",
                api_key="fake_key"
            )
        )

    def create_anthropic_generator() -> DatasetGenerator:
        return DatasetGenerator(
            model_config=ModelConfig(
                provider=ModelProvider.ANTHROPIC,
                name="claude-3-haiku-20240307",
                api_key="fake_key"
            )
        )

    # Creating OpenAI generator should not raise an exception
    openai_generator = create_openai_generator()
    assert openai_generator is not None

    # Creating Anthropic generator should raise an exception
    with pytest.raises(NotImplementedError):
        create_anthropic_generator()
