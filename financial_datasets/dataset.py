from typing import List

from pydantic.main import BaseModel


class DatasetItem(BaseModel):
    question: str
    answer: str
    context: str


class Dataset(BaseModel):
    items: List[DatasetItem]
