"""
This module sets up the Flask application and defines routes to fetch groups and students
from the database.
"""

from flask import Flask, jsonify
from db import Session, Group, Student

app = Flask(__name__)


@app.route("/groups", methods=["GET"])
def get_groups():
    """
    Retrieve a list of groups from the database and return as JSON.

    Returns:
        JSON response containing a list of groups with their id and name.
    """
    with Session() as session:
        groups = session.query(Group).all()
        result = [{"id": group.id, "name": group.name} for group in groups]
        return jsonify(result)


@app.route("/students", methods=["GET"])
def get_students():
    """
    Retrieve a list of students from the database and return as JSON.

    Returns:
        JSON response containing a list of students with their id, name, and email.
    """
    with Session() as session:
        students = session.query(Student).all()
        result = [
            {"id": student.id, "name": student.name, "email": student.email}
            for student in students
        ]
        return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
