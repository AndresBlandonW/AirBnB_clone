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
        from models.amenity import Amenity
        from models.state import State

        classes = {"BaseModel": BaseModel, "User": User,
                   "Place": Place, "State": State, "City": City,
                   "Amenity": Amenity, "Review": Review}

        try:
            with open(self.__file_path) as saved_data:
                new_dict = json.load(saved_data)
                for k, v in new_dict.items():
                    for key in classes.keys():
                        if str(new_dict[k]['__class__']) == key:
                            new_obj = classes[key](**v)
                            key = str((type(new_obj).__name__) +
                                      '.' + (new_obj.id))
                            self.__objects.update({key: new_obj})
                            break
        except FileNotFoundError:
            pass
