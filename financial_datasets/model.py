from enum import Enum

from pydantic.main import BaseModel


class ModelProvider(str, Enum):
    OPEN_AI = 'OPEN_AI'
    ANTHROPIC = 'ANTHROPIC'
    GOOGLE = 'GOOGLE'
    MISTRAL = 'MISTRAL'


class ModelConfig(BaseModel):
    name: str
    api_key: str
    provider: ModelProvider
