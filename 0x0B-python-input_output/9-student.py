#!/usr/bin/python3
"""
Defining a class Student
"""


class Student:
    """Representation of a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.

        Returns:
        - Student: A new Student instance.
        """
        self.data = {
            'first_name': first_name,
            'last_name': last_name,
            'age': age
        }

    def to_json(self):
        """
        Returns a dictionary representation of a Student instance.

        Returns:
        - dict: A dictionary containing the attributes of the Student instance.
        """
        return self.data
