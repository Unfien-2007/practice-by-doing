"""
Week 7 – REST API with Flask
------------------------------
A simple Book Library API demonstrating CRUD endpoints.

Requirements:
    pip install flask

Run:
    python app.py
"""

from flask import Flask, jsonify, request

# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------

def create_app(initial_books: list[dict] | None = None) -> Flask:
    """Create and configure the Flask application.

    *initial_books* is useful for testing so each test starts with a known
    state without touching module-level globals.
    """
    app = Flask(__name__)

    # In-memory store; each item: {id, title, author, year}
    books: list[dict] = list(initial_books) if initial_books else []
    next_id: list[int] = [1]  # mutable container so closures can update it

    def _find(book_id: int) -> dict | None:
        return next((b for b in books if b["id"] == book_id), None)

    # ------------------------------------------------------------------
    # Routes
    # ------------------------------------------------------------------

    @app.get("/books")
    def list_books():
        return jsonify(books), 200

    @app.get("/books/<int:book_id>")
    def get_book(book_id: int):
        book = _find(book_id)
        if book is None:
            return jsonify({"error": "Book not found"}), 404
        return jsonify(book), 200

    @app.post("/books")
    def add_book():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        title = data.get("title", "").strip()
        author = data.get("author", "").strip()
        year = data.get("year")

        if not title or not author:
            return jsonify({"error": "'title' and 'author' are required"}), 400

        if year is not None and not isinstance(year, int):
            return jsonify({"error": "'year' must be an integer"}), 400

        book = {"id": next_id[0], "title": title, "author": author, "year": year}
        next_id[0] += 1
        books.append(book)
        return jsonify(book), 201

    @app.put("/books/<int:book_id>")
    def update_book(book_id: int):
        book = _find(book_id)
        if book is None:
            return jsonify({"error": "Book not found"}), 404

        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        if "title" in data:
            book["title"] = str(data["title"]).strip()
        if "author" in data:
            book["author"] = str(data["author"]).strip()
        if "year" in data:
            if data["year"] is not None and not isinstance(data["year"], int):
                return jsonify({"error": "'year' must be an integer"}), 400
            book["year"] = data["year"]

        return jsonify(book), 200

    @app.delete("/books/<int:book_id>")
    def delete_book(book_id: int):
        book = _find(book_id)
        if book is None:
            return jsonify({"error": "Book not found"}), 404
        books.remove(book)
        return jsonify({"message": "Book deleted"}), 200

    return app


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import os

    app = create_app()
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug)
