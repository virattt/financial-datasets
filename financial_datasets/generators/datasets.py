from typing import List

from pydantic.main import BaseModel


class QuestionAnswer(BaseModel):
    question: str
    answer: str
    context: str


class Dataset(BaseModel):
    questions_answers: List[QuestionAnswer]


class DatasetGenerator:
    def __init__(
        self,
        model_name: str,
        model_api_key: str,
    ):
        self._model_name = model_name
        self._model_api_key = model_api_key

    def generate(self, texts: List[str]) -> Dataset:
        pass
