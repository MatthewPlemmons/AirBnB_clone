#!/usr/bin/python3
import json
import datetime
import os
import models

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        FileStorage.__objects[obj.id] = obj

    def save(self):

        #import pdb; pdb.set_trace()

        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_json()
            # Maybe turn datetime obj in new_dict to str here
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as fd:
                json_dict = json.load(fd)
                for key in json_dict.keys():
                    value = json_dict[key]
                    class_name = value["__class__"]
                    if "BaseModel" in class_name:
                        FileStorage.__objects[key] = models.BaseModel(json_dict[key])
                    if "User" in class_name:
                        FileStorage.__objects[key] = models.User(json_dict[key])
                    if "State" in class_name:
                        FileStorage.__objects[key] = models.State(json_dict[key])
                    if "City" in class_name:
                        FileStorage.__objects[key] = models.City(json_dict[key])
                    if "Amenity" in class_name:
                        FileStorage.__objects[key] = models.Amenity(json_dict[key])
                    if "Place" in class_name:
                        FileStorage.__objects[key] = models.Place(json_dict[key])
                    if "Review" in class_name:
                        FileStorage.__objects[key] = models.Review(json_dict[key])
        except Exception as e:
            pass
