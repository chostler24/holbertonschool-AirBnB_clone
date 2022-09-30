#!/usr/bin/python3
"""console.py module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class defining console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program"""
        return True

    def do_empty_line(self, arg):
        """empty line + ENTER does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
