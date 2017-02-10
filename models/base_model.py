#!/usr/bin/python3
import uuid
import datetime

class BaseModel:

    id = uuid.uuid4()
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def save(self):
        updated_at = datetime.datetime.now()

    def to_json(self):
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)

    def __str__(self):
        return ("{} {} {}".format(type(self).__name__, self.id, BaseModel.__dict__))


my_model = BaseModel()
print(my_model.to_json())
