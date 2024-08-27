"""
This module defines a one-to-one relationship between Parent and Child using SQLAlchemy ORM.
"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base


class Parent(Base):
    """
    Represents a parent entity in a one-to-one relationship with Child.
    """

    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    child: Mapped["Child"] = relationship(
        "Child", back_populates="parent", uselist=False
    )


class Child(Base):
    """
    Represents a child entity in a one-to-one relationship with Parent.
    """

    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship(
        "Parent", back_populates="child", uselist=False
    )
