#!/usr/bin/python3
"""console.py module for tasks 7-8"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


valid_class = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review
               }


class HBNBCommand(cmd.Cmd):
    """class defining console as HBNBCommand for its name"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        """Empty line + Enter does nothing\n"""
        pass

    def do_create(self, args):
        """Create a new object"""
        if len(args) == 0:
            print("** class name missing **")
        elif args not in valid_class.keys():
            print("** class doesn't exist **")
        else:
            object = valid_class[args]()
            print(object.id)
            object.save()

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in valid_class.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        try:
            new_object = FileStorage._FileStorage__objects[
                f"{args[0]}.{args[1]}"]
            print(new_object)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes instance based on id"""
        obj_ect = BaseModel()
        if len(args) == 0:
            print("** class doesn't exist **")
        elif len(obj_ect.__class__.__name__) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            del FileStorage.__objects

    def do_all(self):
        """Prints all string representation of all instances"""
        obj_ect = BaseModel()
        print(str(obj_ect))

    def do_update(self):
        """Updates an instance based on the class name"""
        obj_ect = BaseModel()
        print(obj_ect)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
