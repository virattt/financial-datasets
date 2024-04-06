# Financial Datasets 🧪

Financial Datasets is an open-source Python library 
that allows developers to create synthetic financial datasets
using Large Language Models (LLMs). With this library,
you can generate realistic financial datasets based on SEC filings
such as 10-Ks, 10-Qs, and other financial reports.

[![Twitter Follow](https://img.shields.io/twitter/follow/virattt?style=social)](https://twitter.com/virattt)

## Features

- Generate synthetic financial datasets using LLMs
- Supports various SEC filings (10-Ks, 10-Qs, etc.)
- Easy integration with Python projects
- Customizable data generation options

## Usage

**Example code:**
```python
from financial_datasets.generator import DatasetGenerator

texts = ...  # List of texts from SEC filing
generator = DatasetGenerator(
   model="gpt-4-0125-preview",
   api_key="YOUR_OPENAI_API_KEY",
)
dataset = generator.generate_from_texts(texts, max_questions=100)
```

**Example generated dataset:**
```json
[
  {
    "question": "What was Airbnb's revenue in 2023?",
    "answer": "$9.9 billion",
    "context": "In 2023, revenue increased by 18% to $9.9 billion compared to 2022, primarily due to a 14% increase in Nights and Experiences Booked of 54.5 million combined with higher average daily rates driving a 16% increase in Gross Booking Value of $10.0 billion."
  },
  {
    "question": "By what percentage did Airbnb's net income increase in 2023 compared to the prior year?",
    "answer": "153%",
    "context": "Net income in 2023 increased by 153% to $4.8 billion, compared to the prior year, driven by our revenue growth, increased interest income, discipline in managing our cost structure, and the release of a portion of our valuation allowance on deferred tax assets of $2.9 billion."
  }
]
```

A full end-to-end code example can be found [here](https://colab.research.google.com/gist/virattt/f9b5a0ae82cc0caab57df5dedc2927c9/intro-financial-datasets.ipynb).
## Installation

### Using pip

You can install the Financial Datasets library using pip:

```
pip install financial-datasets
```

### Using Poetry

If you prefer to use Poetry for dependency management, you can add Financial Datasets to your project:

```
poetry add financial-datasets
```

### From the Repository

If you want to install the library directly from the repository, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/financial-datasets.git
   ```

2. Navigate to the project directory:
   ```
   cd financial-datasets
   ```
   
3. Install the dependencies using Poetry:
   ```
   poetry install
   ```

4. You can now use the library in your Python projects.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, 
please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](link-to-license-file).

## Contributors

<a href="https://github.com/virattt/financial-datasets/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=virattt/financial-datasets" />
</a>