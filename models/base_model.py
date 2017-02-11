#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    """Class for BaseModel"""
    def __init__(self, *args, **kwargs):
        for arg in args:
           if type(arg) is dict:
               self.__dict__ = arg
               self.__dict__["created_at"] = datetime.datetime.strptime
               (self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
               self.__dict__["updated_at"] = datetime.datetime.strptime
               (self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
           else:
               self.id = str(uuid.uuid4())
               self.created_at = datetime.datetime.now()
               storage.new(self)

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


my_model = BaseModel()
print(my_model.to_json())
print("_" * 40)
#print(str(my_model))
#print(my_model.id)
#print(my_model.__repr__())
#print(int.__add__(1,2))
#print(str.__len__("hello"))

for items in my_model.__dict__:
    print (items)
