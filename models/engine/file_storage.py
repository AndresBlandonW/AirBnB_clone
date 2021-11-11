#!/usr/bin/python3
"""The file storage engine"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        key = str((type(obj).__name__) + '.' + (obj.id))
        return self.__objects.update({key: obj})
    
    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as fp:
            new_dict = {}

            for k, v in self.__objects.items():
                new_dict.update({k: v.to_dict()})

            json.dump(new_dict, fp)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        try:
            with open(self.__file_path, mode="r") as file:
                dict = json.loads(file.read())
            for key in dict.keys():
                class_name = dict[key]['__class__']
                self.new(eval(class_name)(**dict[key]))
        except:
            pass
