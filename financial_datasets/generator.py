import time
from typing import List

from instructor import patch
from openai import OpenAI

from financial_datasets.dataset import Dataset
from financial_datasets.model import ModelConfig, ModelProvider

system_prompt = """
You are an expert at generating question and ground truth answer pairs for a given block of text. 
Your ground truth answers are always grounded in the content that is in the text.  
You must never make up or hallucinate the ground truth answers.  
Finally, include the 'context' paragraph from where you generated the question and ground truth answer pair.
The `context` paragraph MUST include the context of the ground truth answer that was generated.
"""


class DatasetGenerator:
    def __init__(self, model_config: ModelConfig):
        if model_config.provider != ModelProvider.OPEN_AI:
            raise NotImplementedError(f'Provider {model_config.provider} is not supported yet.')

        self._client = patch(OpenAI())
        self._model_name = model_config.name

    def generate(self, texts: List[str]) -> List[Dataset]:
        max_questions = 10
        datasets = []

        for index, doc in enumerate(texts):
            print(f"Generating questions for batch {index + 1}")

            try:
                # Generate questions
                response = self._client.chat.completions.create(
                    model=self._model_name,
                    response_model=Dataset,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Generate {max_questions / len(texts)} questions for the following block of text: {doc.page_content}"}
                    ],
                )

                # Add the generated questions to our total list of questions
                datasets.append(response)
            except Exception as e:
                print(f"Failed to generate questions for batch {index + 1}: {e}")
                continue

            # Sleep for 1 second to avoid overloading the LLM
            time.sleep(1)

        return datasets
