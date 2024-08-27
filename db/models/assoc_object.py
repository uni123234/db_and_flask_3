"""
This module contains SQLAlchemy models for associations and hierarchical relationships.
"""

from typing import List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base


class Association(Base):
    """
    Represents an association between Parent and Child entities.
    """

    __tablename__ = "association_table"

    left_id: Mapped[int] = mapped_column(ForeignKey("left_table.id"), primary_key=True)
    right_id: Mapped[int] = mapped_column(
        ForeignKey("right_table.id"), primary_key=True
    )
    extra_data: Mapped[Optional[str]]
    child: Mapped["Child"] = relationship()


class Parent(Base):
    """
    Represents a parent entity that can have multiple associations.
    """

    __tablename__ = "left_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List["Association"]] = relationship()


class Child(Base):
    """
    Represents a child entity that can be associated with multiple parents.
    """

    __tablename__ = "right_table"

    id: Mapped[int] = mapped_column(primary_key=True)
