"""
This module defines a many-to-one relationship between Parent and Child using SQLAlchemy.
"""

from typing import Optional
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base


class Parent(Base):
    """
    Represents a parent in a many-to-one relationship with Child.
    """

    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    child_id: Mapped[Optional[int]] = mapped_column(ForeignKey("child_table.id"))
    child: Mapped[Optional["Child"]] = relationship("Child", back_populates="parent")


class Child(Base):
    """
    Represents a child in a many-to-one relationship with Parent.
    """

    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    parent: Mapped[Optional["Parent"]] = relationship("Parent", back_populates="child")
