from typing import List


def generate_dataset() -> List[dict]:
    return [
        {
            "type": "function",
            "function": {
                "name": 'generate_dataset',
                "description": 'This function generates a list of dataset items. Each dataset item has a question, answer, and context',
                "parameters": {
                    "type": 'object',
                    "properties": {
                        "dataset_items": {
                            "type": 'array',
                            "items": {
                                "type": 'object',
                                "properties": {
                                    "question": {
                                        "type": 'string',
                                        "description": 'The generated question.',
                                    },
                                    "answer": {
                                        "type": 'string',
                                        "description": 'The generated answer.',
                                    },
                                    "context": {
                                        "type": 'string',
                                        "description": "The context that the question and answer are generated from.",
                                    },
                                },
                                "required": ['question', 'answer', 'context'],
                            },
                        }
                    },
                    "required": ['dataset_items'],
                },
            }
        }
    ]
