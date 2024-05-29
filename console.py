#!/usr/bin/env python3

import cmd
from models.base_model import storage, BaseModel

class HBNBCommand(cmd.Cmd):
    """ A console that contains the entry point of the command interpreter """
    prompt = '(hbnb)'

    def do_create(self, arg):
        """ a method that helps create an instance of any class """
        if not arg:
            print('** class name missing **')
            return
        try:
            create = globals()[arg]()
            create.save()
            print(create.id)
        except KeyError:
            print("** class doesn't exist **")




    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]


        # Check if class exists
        if class_name not in globals():
            print("** class doesn't exist **")
            return False
        
        # Construct the key and check if instance exists in storage
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return False
        
        # Print the instance
        print(storage.all()[key])


   

        

    def do_EOF(self, line):
        """ a command the helps exit the program"""
        return True
    
    def help_EOF(self):
        print('EOF command to exit the program')
        print('usage: press ctrl+d')
    
    def help_quit(self):
        print('A command thats helps exit the program')
        print('usage: quit')

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True
    
    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()