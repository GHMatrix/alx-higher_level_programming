#!/usr/bin/python3
"""
Defining class Student
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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance.

        Parameters:
        attrs (list, optional): A list of attribute
        names to be retrieved. Defaults to None.

        Returns:
        dict: A dictionary containing the specified
        attributes of the Student instance,
                or all attributes if no specific ones are provided.
        """
        if attrs is None or not isinstance(attrs, list):
            # If attrs is not provided or not a list, retrieve all attributes
            return self.__dict__
        else:
            # Retrieve only the specified attributes
            return {attr: getattr(self, attr, None) for attr in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using a dictionary representation.

        Parameters:
        - json (dict): A dictionary containing attribute
        names as keys and corresponding values.

        Returns:
        - None
        """
        for key, value in json.items():
            setattr(self, key, value)
