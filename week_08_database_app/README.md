# Week 8: Database-Backed CLI App (SQLite + SQLAlchemy)

**Difficulty:** Advanced

## Learning Goals
- Model relational data with SQLAlchemy ORM
- Perform CRUD operations against a SQLite database
- Structure a larger project across multiple modules
- Write integration tests using an in-memory database
- Apply the repository pattern to separate database logic from CLI logic

## Project Description
Build a **Contact Book** CLI application backed by SQLite.  Users can add,
search, update, and delete contacts.  Each contact stores a name, phone number,
e-mail address, and optional notes.

## Concepts Covered
- SQLAlchemy ORM (declarative models, sessions, relationships)
- SQLite database file management
- Repository / data-access layer pattern
- argparse for CLI argument parsing
- Context managers for session lifecycle

## Setup
```bash
pip install sqlalchemy
```

## How to Run
```bash
# Add a contact
python cli.py add --name "Alice Smith" --phone "555-1234" --email "alice@example.com"

# List all contacts
python cli.py list

# Search contacts
python cli.py search --query "alice"

# Update a contact
python cli.py update --id 1 --phone "555-9999"

# Delete a contact
python cli.py delete --id 1
```

## Challenges
1. Add contact groups / tags with a many-to-many relationship.
2. Import/export contacts from/to a vCard (.vcf) file.
3. Add fuzzy name matching for the search command.
