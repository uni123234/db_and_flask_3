"""
This module contains SQLAlchemy models and base class definitions.
"""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from .student import Student
from .group import Group


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.

    Provides a default `id` column and a method to derive table names.
    """

    @classmethod
    @property
    def __tablename__(cls) -> str:
        return str(cls.__name__).lower() + "s"

    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"
