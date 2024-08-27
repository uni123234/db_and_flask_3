"""
This module contains functions for initializing, updating, and selecting data
from the database. It includes functionality for setting up initial data and
performing updates and queries on the database.
"""

from sqlalchemy import select


from db import Session, Group, Student, init_db


def init_data():
    """
    Initialize the database with sample groups and students.
    """
    with Session() as session:
        group1y_5 = Group(name="Python 1y_5_23_3")
        group1y_7 = Group(name="Python 1y_7_22")
        group1y_2 = Group(name="Python 1y_2_22")

        group1y_7.students.extend(
            [
                Student(name="Андрій", second_name="Яцура", email=f"example{i}@mail.io")
                for i in range(10)
            ]
        )
        group1y_2.students.extend(
            [
                Student(
                    name="Андрій", second_name="Яцура", email=f"example2{i}@mail.io"
                )
                for i in range(5)
            ]
        )
        group1y_5.students.extend(
            [
                Student(
                    name="Андрій", second_name="Яцура", email=f"example3{i}@mail.io"
                )
                for i in range(5)
            ]
        )

        session.add_all([group1y_7, group1y_2, group1y_5])
        session.commit()


def update_data():
    """
    Update the name of a group in the database.
    """
    with Session() as session:
        request = select(Group).where(Group.name.like("%1y_5_23_3%"))
        group = session.scalars(request).one()
        group.name = "New name2"
        session.commit()


def select_data():
    """
    Select students from the database and update their email addresses.
    """
    with Session() as session:
        request = select(Student).where(Student.email.like("example3%"))
        result = session.scalars(request).all()
        print(result)
        if result:
            result[0].email = "malva.scrot@example.io"
            session.commit()


def main():
    """
    Main function to initialize the database, populate it with data,
    and perform select and update operations.
    """
    init_db()
    init_data()
    select_data()
    update_data()


if __name__ == "__main__":
    main()
