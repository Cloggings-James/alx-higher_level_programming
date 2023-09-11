#!/usr/bin/python3
"""
Module for the Base class.
"""
import json


class Base:
    """
    The Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.
        Args:
            id (int): The ID of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.
        Args:
            list_dictionaries (list): List of dictionaries.
        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of instances to a file in JSON format.
        Args:
            list_objs (list): List of instances.
        """
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.
        Args:
            json_string (str): JSON string.
        Returns:
            list: List of dictionaries represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a file in JSON format and returns a list of instances.
        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_data = file.read()
                json_list = cls.from_json_string(json_data)
                instances = []
                for item in json_list:
                    instance = cls.create(**item)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance using a dictionary of attributes.
        Args:
            dictionary (dict): Dictionary of attributes.
        Returns:
            Base: New instance of the class with attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            new_instance = None
        new_instance.update(**dictionary)
        return new_instance

