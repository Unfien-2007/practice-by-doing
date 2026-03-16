"""
Week 8 – Repository layer
--------------------------
All database interactions live here, keeping the CLI and models clean.
"""

from sqlalchemy.orm import Session

from .models import Contact


class ContactRepository:
    """CRUD operations for the Contact model."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, name: str, phone: str = "", email: str = "", notes: str = "") -> Contact:
        contact = Contact(name=name, phone=phone, email=email, notes=notes)
        self._session.add(contact)
        self._session.commit()
        self._session.refresh(contact)
        return contact

    def get_all(self) -> list[Contact]:
        return self._session.query(Contact).order_by(Contact.id).all()

    def get_by_id(self, contact_id: int) -> Contact | None:
        return self._session.get(Contact, contact_id)

    def search(self, query: str) -> list[Contact]:
        """Return contacts whose name, email, or phone contains *query*."""
        pattern = f"%{query}%"
        return (
            self._session.query(Contact)
            .filter(
                Contact.name.ilike(pattern)
                | Contact.email.ilike(pattern)
                | Contact.phone.ilike(pattern)
            )
            .order_by(Contact.id)
            .all()
        )

    def update(self, contact_id: int, **kwargs) -> Contact | None:
        """Update allowed fields on the contact. Returns None if not found."""
        contact = self.get_by_id(contact_id)
        if contact is None:
            return None
        allowed = {"name", "phone", "email", "notes"}
        for key, value in kwargs.items():
            if key in allowed:
                setattr(contact, key, value)
        self._session.commit()
        self._session.refresh(contact)
        return contact

    def delete(self, contact_id: int) -> bool:
        """Delete a contact. Returns True on success, False if not found."""
        contact = self.get_by_id(contact_id)
        if contact is None:
            return False
        self._session.delete(contact)
        self._session.commit()
        return True
