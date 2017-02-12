#!/usr/bin/python3
import cmd
import sys
import os
import models

class Console(cmd.Cmd):
    """ Console Interpreter"""
    prompt = "(hbnb)"

    def do_exit(self, args):
        """Exits the  Console"""
        return (-1)

    def do_EOF(self, args):
        """Exits system with end of file character 'control' + 'c'"""
        return (self.do_exit(args))

    def do_shell(self, args):
        """Pass system shell if line starts with '!' character"""
        os.system(args)

    def do_help(self, args):
        """Gets help command if 'help' or '?' is passed"""
        cmd.Cmd.do_help(self, args)

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

    def emptyline(self):
        '''Prevents repeat of previous input.'''
        pass

    def do_create(self, args):
        model = {"BaseModel" : models.BaseModel(), "User" : models.User(),
                 "State": models.State(), "City" : models.City(),
                 "Amenity" : models.Amenity(), "Place" : models.Place(),
                 "Review" : models.Review()}
        if len(args) < 1:
            print("** class name missing **")
        else:
            if args in model.keys():
                value = model[args]
                new = value
                new.save()
                print(new.id)

if __name__ == "__main__":
    prompts = Console()
    prompts.cmdloop()
