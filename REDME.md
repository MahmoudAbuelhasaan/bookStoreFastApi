# Book Store FastAPI Application

This is a RESTful API application for managing a bookstore using FastAPI framework.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL database

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd bookStoreFastApi
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database:
   - Create a `.env` file in the root directory
   - Add your database credentials:
```
DATABASE_URL=postgresql://username:password@localhost:5432/bookstore
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. Access the API documentation:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## API Endpoints

- `GET /books/` - List all books
- `POST /books/` - Create a new book
- `GET /books/{id}` - Get book details
- `PUT /books/{id}` - Update book
- `DELETE /books/{id}` - Delete book

## Project Structure

```
bookStoreFastApi/
├── api/
│   ├── __init__.py
│   └── book.py
├── core/
│   ├── __init__.py
│   └── database.py
├── models/
│   └── __init__.py
├── schemas/
│   └── __init__.py
├── main.py
├── requirements.txt
└── README.md
```

## Development

To run tests:
```bash
pytest
```

## License

This project is licensed under the MIT License.