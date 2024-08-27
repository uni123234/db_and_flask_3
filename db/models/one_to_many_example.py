"""
This module defines a one-to-many relationship between Parent and Child using SQLAlchemy.
"""

from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base


class Parent(Base):
    """
    Represents a parent entity in a one-to-many relationship with Child.
    """

    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List["Child"]] = relationship(
        "Child", back_populates="parent", cascade="all, delete-orphan"
    )


class Child(Base):
    """
    Represents a child entity in a one-to-many relationship with Parent.
    """

    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship("Parent", back_populates="children")
