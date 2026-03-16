# Week 7: REST API with Flask

**Difficulty:** Advanced

## Learning Goals
- Build a RESTful HTTP API using Flask
- Design CRUD endpoints following REST conventions
- Use JSON request/response bodies
- Handle errors and return appropriate HTTP status codes
- Test endpoints with `pytest` and `Flask`'s test client

## Project Description
Build a simple **Book Library API** with full CRUD support:

| Method | Endpoint          | Description          |
|--------|-------------------|----------------------|
| GET    | `/books`          | List all books       |
| GET    | `/books/<id>`     | Get a single book    |
| POST   | `/books`          | Add a new book       |
| PUT    | `/books/<id>`     | Update a book        |
| DELETE | `/books/<id>`     | Delete a book        |

Books are stored in memory (no database required yet).

## Concepts Covered
- Flask routing and view functions
- HTTP methods and status codes
- `request.get_json()` and `jsonify()`
- Input validation
- Flask application factory pattern

## Setup
```bash
pip install flask
```

## How to Run
```bash
python app.py
# Server starts at http://127.0.0.1:5000
```

## Example Requests
```bash
# Add a book
curl -X POST http://127.0.0.1:5000/books \
     -H "Content-Type: application/json" \
     -d '{"title": "Clean Code", "author": "Robert Martin", "year": 2008}'

# List all books
curl http://127.0.0.1:5000/books
```

## Challenges
1. Persist books to a JSON file instead of keeping them in memory.
2. Add search/filter via query parameters (e.g. `?author=Martin`).
3. Add pagination (`?page=1&per_page=10`).
