#!/usr/bin/python3
"""
Defining a class Student
"""


class Student:
    """
    Representation of a student
    """

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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance.

        Parameters:
        attrs (list, optional): A list of attribute names
        to be retrieved. Defaults to None.

        Returns:
        dict: A dictionary containing the specified
        attributes of the Student instance,
                or all attributes if no specific ones are provided.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
