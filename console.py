#!/usr/bin/python3
""" creating class HBNBCommand"""
import cmd
import shlex
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

props = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
         "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ Class that contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ exit of command interpreter"""
        return True

    def do_EOF(self, arg):
        """ exit of command interpreter"""
        print("")
        return True

    def emptyline(self):
        """ this is for the case for an empty line + ENTER
        shouldn’t execute anything"""
        return False

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id

        Syntax:
            create [name]

        Example:
            $ create BaseModel"""
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
            """ Prints the string representation of an instance
            Syntax:
                    show [name] [id]

            Example:
                    $ show BaseModel 1234-1234-1234"""
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
        """ Deletes an instance based on the class name and id

        Syntax:
            destroy [name] [id]

        Example:
            $ destroy BaseModel 1234-1234-1234"""
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
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name

        Syntax:
            all [name]

        Example:
            $ all BaseModel or $ all"""
        arg_list = shlex.split(arg)
        lista_obj = []
        if len(arg_list) == 0:
            for valor in models.storage.all().values():
                lista_obj.append(str(valor))
            print("[", end="")
            print(", ".join(lista_obj), end="")
            print("]")
        elif arg_list[0] in props:
            for clave in models.storage.all():
                if arg_list[0] in clave:
                    aux = str(models.storage.all()[clave])
                    lista_obj.append(aux)
            print("[", end="")
            print(", ".join(lista_obj), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Command that update a class.

        Syntax:
            update <class name> <id> <at name> "<at value>

        Ex.:
            $ update User 1234-1234-1234 email "aibnb@hbtn.com
        """
        arg_list = shlex.split(arg)
        intlist = ("number_rooms", "number_bathrooms", "max_guest",
                   "price_by_night")
        floatlist = ("latitude", "longitude")
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in props:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            clave = arg_list[0] + "." + arg_list[1]
            if clave not in models.storage.all():
                print("** no instance found **")
            elif len(arg_list) == 2:
                print("** attribute name missing **")
            elif len(arg_list) == 3:
                print("** value missing **")
            else:
                if arg_list[0] == "Place":
                    if arg_list[2] in intlist:
                        try:
                            arg_list[3] = int(arg_list[3])
                        except:
                            arg_list[3] = 0
                    elif arg_list[2] in floatlist:
                        try:
                            arg_list[3] = float(arg_list[3])
                        except:
                            arg_list[3] = 0.0
                setattr(models.storage.all()[clave], arg_list[2], arg_list[3])
                models.storage.all()[clave].save()

    def do_count(self, arg):
        """ Command that count the number of intances of
        each class

        Syntax:
            count <class name>

        Example:
            $ count User"""
        if arg == "":
            print("** class name missing **")
            return
        arg_list = shlex.split(arg)
        if arg_list[0] not in props:
            print("** class doesn't exist **")
            return
        dict_obj = storage.all()
        ret = 0
        for i, valor in dict_obj.items():
            if dict_obj[i].__class__.__name__ == arg_list[0]:
                ret += 1
        print(ret)

    def default(self, arg):
        """la puta que lo aprio"""
        dot_found = re.search(r"\.", arg)
        dict_arg = {"all": self.do_all,
                    "create": self.do_create,
                    "destroy": self.do_destroy,
                    "show": self.do_show,
                    "update": self.do_update,
                    "count": self.do_count}
        if dot_found:
            commas = [arg[:dot_found.span()[0]],
                      arg[dot_found.span()[1]:]]
            parser = re.search(r"\((.*?)\)", commas[1])
            if parser:
                comando = [commas[1][:parser.span()[0]], parser.group()[1:-1]]
                if comando[0] == "update":
                    rem_com = comando[1].replace(",", "")
                    call = "{} {}".format(commas[0], rem_com)
                    return dict_arg[comando[0]](call)
                elif comando[0] in dict_arg.keys():
                    call = "{} {}".format(commas[0], comando[1])
                    return dict_arg[comando[0]](call)
        print("*** Unknwon syntax: {}".format(arg))
        return False

    def postloop(self):
        """la puta que lo aprio"""
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()
