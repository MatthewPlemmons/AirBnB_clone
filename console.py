#!/usr/bin/python3
import cmd, sys, os



class Console(cmd.Cmd):
    """ Console Interpreter"""
    prompt = "(hbnb)"

    def do_hist(self, args):
        """Prints history of commands entered"""
        print (self._hist)

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

    def preloop(self):
        cmd.Cmd.preloop(self)
        self.__hist = []
        self.__locals = {}
        self.__globals = {}

if __name__ == "__main__":
    prompt = Console()
    prompt.cmdloop()
