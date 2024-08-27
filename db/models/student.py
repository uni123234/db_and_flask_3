"""
This module defines the Student model for use with SQLAlchemy ORM.
"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base
from .group import (
    Group,
)


class Student(Base):
    """
    Represents a student who is related to a group in a many-to-one relationship.
    """

    name: Mapped[str] = mapped_column()
    second_name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship("Group", back_populates="students")

    def __repr__(self) -> str:
        return f"<{super().__repr__()}: {self.second_name} {self.name}>"
