
# Wikipedia Word‑Frequency API

This project implements a FastAPI application that crawls a Wikipedia article (and optionally its linked articles up to a given depth) and generates a word‑frequency dictionary. It also provides an endpoint for extracting filtered keywords based on an ignore list and percentile threshold. The assignment explicitly allowed the use of AI tools, and the project was built with clarity, readability, and testability in mind.

## Features

- Traverse Wikipedia articles up to a specified depth  
- Extract visible text and compute word frequencies  
- Filter words by ignore list and percentile  
- Two API endpoints (`GET /word-frequency` and `POST /keywords`)  
- No authentication or database required  
- Fully tested with `pytest`  
- Lightweight and easy to run locally  

## Requirements

- Python 3.9+  
- pip  
- Virtual environment recommended  

Dependencies are listed in `requirements.txt`.

## Setup

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/DishantGudlani/wikipedia_wordfreq_msci
cd wikipedia_wordfreq_msci
```
Create and activate a virtual environment:

```bash
python3 -m venv wiki_venv
source wiki_venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```
## Running the Server

Start the FastAPI server using Uvicorn:
```bash
uvicorn app:app --reload
```

The API will be available at:
```bash
http://127.0.0.1:8000
```

Interactive API docs (Swagger UI):
```bash
http://127.0.0.1:8000/docs
```

## API Endpoints

- GET /word-frequency

Generate a word‑frequency dictionary from a Wikipedia article.

Query Parameters:
| Name    | Type   | Description                         |
|---------|--------|-------------------------------------|
| article | string | Title of the Wikipedia article      |
| depth   | int    | Traversal depth (0 = only this one) |

Example:
```bash
curl "http://127.0.0.1:8000/word-frequency?article=Python_(programming_language)&depth=1"
```

- POST /keywords <br>
Generate a filtered word‑frequency dictionary.

Request Body:

```bash
Json
{
  "article": "Python (programming language)",
  "depth": 1,
  "ignore_list": ["python", "language"],
  "percentile": 80
}
```

Example:
```bash
curl -X POST "http://127.0.0.1:8000/keywords" \
  -H "Content-Type: application/json" \
  -d '{
        "article": "Python (programming language)",
        "depth": 1,
        "ignore_list": ["python", "language"],
        "percentile": 80
      }'
```

Running Tests
The project includes unit tests for text processing, Wikipedia traversal, and API endpoints.
Run all tests with:
```bash
pytest
```
## Project Structure

```
wikipedia_wordfreq_msci/
│ app.py
│ wikipedia_traversal.py
│ text_processing.py
│ models.py
│ requirements.txt
│ README.md
└── tests/
├── test_api.py
├── test_text_processing.py
├── test_traversal.py
└── init.py
```

Notes
- No authentication is required (per assignment spec)
- No database is used
- Traversal avoids revisiting articles to prevent loops
- Anchor text from links is included in the main article’s text (expected behavior)

