"""Tests for Week 7 – REST API with Flask."""

import json
import pytest
from week_07_rest_api.app import create_app

SAMPLE_BOOK = {"title": "Clean Code", "author": "Robert Martin", "year": 2008}


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def client_with_book():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        client.post("/books", json=SAMPLE_BOOK)
        yield client


def test_list_books_empty(client):
    resp = client.get("/books")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_add_book(client):
    resp = client.post("/books", json=SAMPLE_BOOK)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["title"] == "Clean Code"
    assert data["id"] == 1


def test_add_book_missing_fields(client):
    resp = client.post("/books", json={"title": "No Author"})
    assert resp.status_code == 400


def test_add_book_no_json(client):
    resp = client.post("/books", data="not json")
    assert resp.status_code == 400


def test_get_book(client_with_book):
    resp = client_with_book.get("/books/1")
    assert resp.status_code == 200
    assert resp.get_json()["title"] == "Clean Code"


def test_get_book_not_found(client):
    resp = client.get("/books/999")
    assert resp.status_code == 404


def test_update_book(client_with_book):
    resp = client_with_book.put("/books/1", json={"title": "The Clean Coder"})
    assert resp.status_code == 200
    assert resp.get_json()["title"] == "The Clean Coder"


def test_update_book_not_found(client):
    resp = client.put("/books/999", json={"title": "X"})
    assert resp.status_code == 404


def test_delete_book(client_with_book):
    resp = client_with_book.delete("/books/1")
    assert resp.status_code == 200
    resp2 = client_with_book.get("/books/1")
    assert resp2.status_code == 404


def test_delete_book_not_found(client):
    resp = client.delete("/books/999")
    assert resp.status_code == 404
