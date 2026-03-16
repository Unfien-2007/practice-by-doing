"""Tests for Week 8 – Database-Backed CLI App."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from week_08_database_app.models import Base, Contact
from week_08_database_app.repository import ContactRepository


@pytest.fixture
def repo():
    """Return a ContactRepository backed by an in-memory SQLite database."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield ContactRepository(session)
    session.close()


def test_add_contact(repo):
    c = repo.add(name="Alice", phone="555-1234", email="alice@example.com")
    assert c.id is not None
    assert c.name == "Alice"


def test_get_all_empty(repo):
    assert repo.get_all() == []


def test_get_all(repo):
    repo.add(name="Bob")
    repo.add(name="Carol")
    contacts = repo.get_all()
    assert len(contacts) == 2


def test_get_by_id(repo):
    c = repo.add(name="Dave")
    found = repo.get_by_id(c.id)
    assert found is not None
    assert found.name == "Dave"


def test_get_by_id_missing(repo):
    assert repo.get_by_id(999) is None


def test_search_by_name(repo):
    repo.add(name="Alice Smith")
    repo.add(name="Bob Jones")
    results = repo.search("alice")
    assert len(results) == 1
    assert results[0].name == "Alice Smith"


def test_search_by_email(repo):
    repo.add(name="Eve", email="eve@example.com")
    results = repo.search("example.com")
    assert len(results) == 1


def test_update_contact(repo):
    c = repo.add(name="Frank")
    updated = repo.update(c.id, phone="999-0000")
    assert updated.phone == "999-0000"


def test_update_contact_not_found(repo):
    assert repo.update(999, name="Ghost") is None


def test_delete_contact(repo):
    c = repo.add(name="Grace")
    result = repo.delete(c.id)
    assert result is True
    assert repo.get_by_id(c.id) is None


def test_delete_contact_not_found(repo):
    assert repo.delete(999) is False
