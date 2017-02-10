#!/usr/bin/python3
import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (__objects)

    def new(self, obj):
        FileStorage.__objects[obj.id] = obj

    def save(self):
        new_dict = {}
        for key in self.__objects[keys]:
            new_dict[key] = self.__objects[key].to_json()
        with open(__file_path, "w+") as fh:
            fh.write(dumps(new_dict))

    def reload(self):
        json.load()

from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
print(my_model)