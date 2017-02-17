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
            if args in model:
                model[args].save()
                print(model[args].id)
                return
            else:
                print("** class doesn't exist **")
                return

    def do_show(self, args):
        """Print the string representation of an instance"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in Console.class_names:
            print("** class doesn't exist **")
            return
        all_instances = storage.all()
        if args[1] in all_instances:
            print(all_instances[args[1]])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance"""

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in Console.class_names:
            print("** class doesn't exist **")
            return
        all_model_ids = storage.all()
        if args[1] in list(all_model_ids):
            del all_model_ids[args[1]]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Print string representation of Class instances"""

        if args not in self.class_names:
            print("** class doesn't exist **")
        else:
            all_instances = storage.all()
            for i in all_instances.keys():
                if args == all_instances[i].__class__.__name__:
                    print(str(all_instances[i]))


    def do_update(self, args):
        """Add or change instance attributes"""

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
    Console().cmdloop()
