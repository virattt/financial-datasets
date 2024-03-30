from typing import List

from pydantic.main import BaseModel


class QuestionAnswer(BaseModel):
    question: str
    answer: str
    context: str


class Dataset(BaseModel):
    question_answers: List[QuestionAnswer]
