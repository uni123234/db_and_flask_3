"""
This module defines the Group class and its relationship with Student.
"""

from typing import List
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, relationship
from . import Base
from .student import Student


class Group(Base):
    """
    Represents a group to which multiple students can belong.
    """

    __tablename__ = "group"

    id: Mapped[int] = Column(
        Integer, primary_key=True
    )
    name: Mapped[str] = Column(
        String, nullable=False
    )

    students: Mapped[List["Student"]] = relationship(
        "Student", back_populates="group", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Group(name={self.name})>"
