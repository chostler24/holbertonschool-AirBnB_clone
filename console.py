#!/usr/bin/python3
"""console.py module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class defining console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def empty_line(self):
        """Empty line + Enter does nothing\n"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
