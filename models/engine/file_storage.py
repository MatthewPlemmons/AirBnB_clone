#!/usr/bin/python3
import json
import uuid
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
        new_dict = {}
        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_json()
        with open(FileStorage.__file_path, "w+") as fd:
            json.dump(new_dict, fd)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path) == True:
            with open(FileStorage.__file_path, "r+") as fd:
                json_dict = json.load(fd)
                print(json_dict)
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
