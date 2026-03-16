"""
Week 8 – Database models (SQLAlchemy ORM)
------------------------------------------
Defines the Contact model and helpers for creating a SQLAlchemy engine/session.
"""

from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    phone = Column(String(30), nullable=True)
    email = Column(String(120), nullable=True)
    notes = Column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<Contact id={self.id} name={self.name!r}>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone or "",
            "email": self.email or "",
            "notes": self.notes or "",
        }


def make_engine(db_url: str = "sqlite:///contacts.db"):
    """Create an engine and ensure all tables exist."""
    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)
    return engine


def make_session(engine) -> Session:
    """Return a new session bound to *engine*."""
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()
