"""
Week 8 – Contact Book CLI
---------------------------
argparse-based command-line interface for the contact book application.

Usage examples:
    python cli.py add --name "Alice Smith" --phone "555-1234" --email "alice@example.com"
    python cli.py list
    python cli.py search --query "alice"
    python cli.py update --id 1 --phone "555-9999"
    python cli.py delete --id 1
"""

import argparse
import sys
from pathlib import Path

from .models import make_engine, make_session
from .repository import ContactRepository

DB_PATH = Path(__file__).parent / "contacts.db"


def fmt_contact(contact) -> str:
    d = contact.to_dict()
    parts = [f"[{d['id']}] {d['name']}"]
    if d["phone"]:
        parts.append(f"  Phone: {d['phone']}")
    if d["email"]:
        parts.append(f"  Email: {d['email']}")
    if d["notes"]:
        parts.append(f"  Notes: {d['notes']}")
    return "\n".join(parts)


def cmd_add(repo: ContactRepository, args: argparse.Namespace) -> None:
    contact = repo.add(
        name=args.name,
        phone=args.phone or "",
        email=args.email or "",
        notes=args.notes or "",
    )
    print(f"Contact added:\n{fmt_contact(contact)}")


def cmd_list(repo: ContactRepository, _args: argparse.Namespace) -> None:
    contacts = repo.get_all()
    if not contacts:
        print("No contacts found.")
        return
    for c in contacts:
        print(fmt_contact(c))
        print()


def cmd_search(repo: ContactRepository, args: argparse.Namespace) -> None:
    contacts = repo.search(args.query)
    if not contacts:
        print(f"No contacts matching '{args.query}'.")
        return
    for c in contacts:
        print(fmt_contact(c))
        print()


def cmd_update(repo: ContactRepository, args: argparse.Namespace) -> None:
    updates = {}
    if args.name:
        updates["name"] = args.name
    if args.phone:
        updates["phone"] = args.phone
    if args.email:
        updates["email"] = args.email
    if args.notes:
        updates["notes"] = args.notes

    if not updates:
        print("Nothing to update. Provide at least one field to change.")
        return

    contact = repo.update(args.id, **updates)
    if contact is None:
        print(f"Contact with id {args.id} not found.")
    else:
        print(f"Contact updated:\n{fmt_contact(contact)}")


def cmd_delete(repo: ContactRepository, args: argparse.Namespace) -> None:
    if repo.delete(args.id):
        print(f"Contact {args.id} deleted.")
    else:
        print(f"Contact with id {args.id} not found.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cli.py", description="Contact Book – manage your contacts from the CLI."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # add
    p_add = sub.add_parser("add", help="Add a new contact")
    p_add.add_argument("--name", required=True, help="Full name")
    p_add.add_argument("--phone", help="Phone number")
    p_add.add_argument("--email", help="E-mail address")
    p_add.add_argument("--notes", help="Optional notes")

    # list
    sub.add_parser("list", help="List all contacts")

    # search
    p_search = sub.add_parser("search", help="Search contacts")
    p_search.add_argument("--query", required=True, help="Search term")

    # update
    p_update = sub.add_parser("update", help="Update a contact")
    p_update.add_argument("--id", type=int, required=True, help="Contact ID")
    p_update.add_argument("--name", help="New name")
    p_update.add_argument("--phone", help="New phone")
    p_update.add_argument("--email", help="New email")
    p_update.add_argument("--notes", help="New notes")

    # delete
    p_delete = sub.add_parser("delete", help="Delete a contact")
    p_delete.add_argument("--id", type=int, required=True, help="Contact ID")

    return parser


COMMANDS = {
    "add": cmd_add,
    "list": cmd_list,
    "search": cmd_search,
    "update": cmd_update,
    "delete": cmd_delete,
}


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    engine = make_engine(f"sqlite:///{DB_PATH}")
    session = make_session(engine)
    try:
        repo = ContactRepository(session)
        COMMANDS[args.command](repo, args)
    finally:
        session.close()


if __name__ == "__main__":
    main()
