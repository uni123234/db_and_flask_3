"""
This module defines a many-to-many relationship between Parent and Child using SQLAlchemy.
"""

from typing import List
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import Mapped, relationship
from . import Base

# Association table for many-to-many relationship
association_table = Table(
    "association_table",
    Base.metadata,
    Column("left_id", ForeignKey("left_table.id"), primary_key=True),
    Column("right_id", ForeignKey("right_table.id"), primary_key=True),
)


class Parent(Base):
    """
    Represents the parent in a many-to-many relationship.
    """

    __tablename__ = "left_table"

    id: Mapped[int] = Column(Integer, primary_key=True)
    children: Mapped[List["Child"]] = relationship(
        "Child", secondary=association_table, back_populates="parents"
    )


class Child(Base):
    """
    Represents the child in a many-to-many relationship.
    """

    __tablename__ = "right_table"

    id: Mapped[int] = Column(Integer, primary_key=True)
    parents: Mapped[List["Parent"]] = relationship(
        "Parent", secondary=association_table, back_populates="children"
    )
