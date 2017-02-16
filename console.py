#!/usr/bin/python3
import cmd
import sys
import os
from models import *

"""Shell-like interpreter to handle commandline instructions"""


class Console(cmd.Cmd):
    """Console Interpreter"""
    prompt = "(hbnb) "
    class_names = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]

    def do_exit(self, args):
        """Exit the interpreter"""
        return (-1)

    def do_EOF(self, args):
        """Exit interpreter by entering 'EOF' or pressing Crtl-D"""
        return (self.do_exit(args))

    def do_shell(self, args):
        """Pass system shell if line starts with '!' character"""
        os.system(args)

    def do_help(self, args):
        """Get help command if 'help' or '?' is entered"""
        cmd.Cmd.do_help(self, args)

    def do_quit(self, args):
        """Exit the interpreter"""
        raise SystemExit

    def emptyline(self):
        """Prevents repeat of previous input."""
        pass

    def do_create(self, args):
        """ Creates an instance of a goven model """
        model = {"BaseModel": models.BaseModel(), "User": models.User(),
                 "State": models.State(), "City": models.City(),
                 "Amenity": models.Amenity(), "Place": models.Place(),
                 "Review": models.Review()}
        if len(args) < 1:
            print("** class name missing **")
        else:
            if args in model.keys():
                value = model[args]
                new = value
                new.save()
                print(new.id)

    def do_show(self, args):
        """ Prints the string representation of an instance based on the class
        name and id """
        args = args.split()
        if len(args) <= 0:
            print("** class name missing **")
        if len(args) <= 1:
            print("** instance id missing **")
        if args[0] not in class_name:
            print("** class doesn't exist **")
        else:
            show_all = storage.all()
            for key_id in show_all.keys():
                if key_id == args[1]:
                    print(show_all[key_id])
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = args.split()
        if len(args[0]) == 0:
            print("** class name missing **")
        if len(args[1]) == 0:
            print("** instance id missing **")
        if args[0] not in class_name:
            print("** class doesn't exist **")
        show_all = storage.all()
        for key_id in show_all.keys():
            if key_id == args[1]:
                del show_all[key_id]
                models.storage.save()
        print("** no instance found **")

    def do_all(self, args):
        show_list = []
        store = models.storage.all()

        args = args.split()
        if args[0] not in class_name:
            print("** class doesn't exist **")
        else:
            for key in self.store.keys():
                if self.store[key].__class__.__name__ == args[0]:
                    show_list.append(str(store[key]))
            print(show_list)

    def do_update(self, args):
        """Update an instance based on the class name and id by adding or
        updating attribute"""
        class_names
        args = args.split()
        if len(args) <= 0:
            print("** class name missing **")
        if len(args) <= 1:
            print("** instance id missing **")
        if len(args) <= 2:
            print("** attribute name missing **")
        if len(args) <= 3:
            print("** value missing **")
        stored_obj = models.storage.all()
        for obj_id in stored_obj.keys():
            if obj_id == args[1]:
                setattr(stored_obj[obj_id], args[2], args[3])
                models.storage.save()
            else:
                print("** no instance found **")

if __name__ == "__main__":
    prompts = Console()
    prompts.cmdloop()
