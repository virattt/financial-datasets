from typing import List

from financial_datasets.dataset import Dataset
from financial_datasets.model import ModelConfig


class DatasetGenerator:
    def __init__(self, model_config: ModelConfig):
        self._model_config = model_config

    def generate(self, texts: List[str]) -> Dataset:
        pass
