#!/usr/bin/python3
""" creating class HBNBCommand"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

props = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

class HBNBCommand(cmd.Cmd):
        """ Class that contains the entry point of the command interpreter"""
        prompt = "(hbnb) "
        def do_quit(self, arg):
                """ exit of command interpreter"""
                return True

        def do_EOF(self, arg):
                """ exit of command interpreter"""
                return True

        def emptyline(self):
                """ this is for the case for an empty line + ENTER shouldn’t execute anything"""
                return False

        def do_create(self, arg):
                arg_list = shlex.split(arg)
                if len(arg_list) == 0:
                        print("** class name missing **")
                        return False
                if arg_list[0] in props:
                        instancia = props[arg_list[0]]()
                else:
                        print("** class doesn't exist **")
                        return False
                print(instancia.id)
                instancia.save()

        def do_show(self, arg):
                arg_list = shlex.split(arg)
                if len(arg_list) == 0:
                        print("** class name missing **")
                        return False
                if arg_list[0] not in props:
                        print("** class doesn't exist **")
                else:
                        if len(arg_list) == 1:
                                print("** instance id missing **")
                        else:
                                clave = arg_list[0] + "." + arg_list[1]
                                if clave in models.storage.all():
                                        print(models.storage.all()[clave])
                                else:
                                        print("** no instance found **")

                
        def do_destroy(self, arg):
                arg_list = shlex.split(arg)
                if len(arg_list) == 0:
                        print("** class name missing **")
                elif arg_list[0] in props:
                        if len(arg_list) > 1:
                                clave = arg_list[0] + "." + arg_list[1]
                                if clave in models.storage.all():
                                        models.storage.all().pop(clave)
                                        models.storage.save()
                                else: 
                                        print("** no instance found **")
                        else:
                                print("** instance id missing **")
                else:
                        print("** class name missing **")

        #def do_all(self, arg):


if __name__ == '__main__':
    HBNBCommand().cmdloop()
