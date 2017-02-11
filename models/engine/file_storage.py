#!/usr/bin/python3
import json, models, uuid

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
        if os.path.isfile(FileStorage.__file_path) == True:
            with open(FileStorage.__file_path, "r+") as fd:
               json_dict = json.load(fd)
               for key in json_dict.keys():
                   cls = json_dict[key]
