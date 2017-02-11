#!/usr/bin/python3
import uuid
import datetime
import models

class BaseModel:
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
           if type(arg[0]) is dict:
               self.__dict__ = arg[0]
               self.__dict__["created_at"] = datetime.datetime.strptime
               (self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
               self.__dict__["updated_at"] = datetime.datetime.strptime
               (self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
           else:
               self.id = str(uuid.uuid4())
               self.created_at = datetime.datetime.now()
               models.storage.new(self)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_json(self):
        self.created_at = datetime.datetime.isoformat(self.created_at)
        self.updated_at = datetime.datetime.isoformat(self.updated_at)
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)

    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))
