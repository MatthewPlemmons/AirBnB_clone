#!/usr/bin/python3
import uuid
import datetime
import models

class BaseModel():
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
           if type(args[0]) is dict:
               self.__dict__ = args[0]
               self.__dict__["created_at"] = datetime.datetime.strptime
               (self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
               self.__dict__["updated_at"] = datetime.datetime.strptime
               (self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """ save method

        saves the 'update_at' attribute to Filestorage
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_json(self):
        """ to_json method

        Turns dateime into strings before passing them into a new dict
        Returns new_dict with key value pairs
        """
        str_dict = self.__dict__.copy()
        str_dict['created_at'] = str(str_dict['created_at'])
        str_dict['updated_at'] = str(str_dict['updated_at'])
        str_dict['__class__'] = self.__class__.__name__
        return (str_dict)

    def __str__(self):
        """ __str__ method

        Returns user friendly string
        """
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))
