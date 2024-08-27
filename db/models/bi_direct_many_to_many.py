"""
This module contains SQLAlchemy models for a bidirectional many-to-many relationship between 
Parent and Child entities.
"""

from typing import List
from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base

# Association table for the many-to-many relationship
association_table = Table(
    "association_table",
    Base.metadata,
    Column("left_id", ForeignKey("left_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
)


class Parent(Base):
    """
    Represents a parent entity that can be associated with multiple Child entities.
    """

    __tablename__ = "left_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List["Child"]] = relationship(
        secondary=association_table, back_populates="parents"
    )


class Child(Base):
    """
    Represents a child entity that can be associated with multiple Parent entities.
    """

    __tablename__ = "right_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parents: Mapped[List["Parent"]] = relationship(
        secondary=association_table, back_populates="children"
    )
