#!/usr/bin/python3
""""""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The base model"""
    def __init__(self, *args, **kwargs):
        """Init method
            args: pass arguments
            kwargs pass kwyword arguments
        """
        if len(kwargs) < 1:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        setattr(self, k,
                                datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, k, v)

    def __str__(self):
        """Str method"""
        name = str(self.__class__.__name__)
        msg = "[{}] ({}) {}"
        msg = msg.format(name, self.id, self.__dict__)
        return msg

    def save(self):
        """Save method"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Builds the dict representation of the object"""
        new_dict = {'__class__': self.__class__.__name__}

        for key, value in self.__dict__.items():
            if key == 'created_at':
                time_key = 'created_at'
                time_value = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
                new_dict.update({time_key: time_value})
            elif key == 'updated_at':
                time_key = 'updated_at'
                time_value = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
                new_dict.update({time_key: time_value})
            else:
                new_dict.update({key: value})

        return new_dict
