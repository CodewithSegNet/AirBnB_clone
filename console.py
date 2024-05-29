#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import shlex

class HBNBCommand(cmd.Cmd):
    """ A console that contains the entry point of the command interpreter """
    prompt = '(hbnb)'

    def do_create(self, arg):
        """ a method that helps create an instance of any class """
        if not arg:
            print('** class name missing **')
            return
        try:
            create_new_instance = globals()[arg]()
            create_new_instance.save()
            print(create_new_instance.id)
        except KeyError:
            print("** class doesn't exist **")




    def do_show(self, arg):
        """ a method that shows string representation of an
            instance based on the class name """
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
            return
        
        # Construct the key and check if instance exists in storage
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        
        # Print the instance
        print(storage.all()[key])


    def do_destroy(self, arg):
        """ a method that deletes an instance based on the class name and id """
        if not arg:
            print(" ** class name missing **")
            return

        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print(" ** instance id missing **")
            return
            
        class_name = args[0]
        instance_id = args[1]

        # check if class exists
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        
        # Construct the key and check if instance exists in storage
        key = f'{class_name}.{instance_id}'

        # check if instance exists in storage
        if key not in storage.all():
            print("** no instance found **")
            return
        
        # delete key from storage and update storage afterwords
        del storage.all()[key]
        storage.save()
        print("instance deleted successfully!!!")


    def do_all(self, arg):
        """Prints all string representations of all instances based or not on the class name"""
        if arg and arg not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
            return
        else:
            if arg not in globals():
                print("** class doesn't exist **")
                return
            
            #class name povided exist, print all instances
            class_instances = storage.all().values()
            print([str(instance) for instance in class_instances if arg == '' or arg == type(instance).__name__])
   

    def do_update(self, arg):
        """ a method that Updates an instance based on the class name 
            and id by adding or updating attribute """
        if not arg:
            print(" *** class name missing ***")

        try:
            args = shlex.split(arg)
        except ValueError:
            print('** invalid command **')
            return

        args = arg.split()

        if len(args) < 1:
            print(" *** class name missing ***")
            return
        if len(args) < 2:
            print(" *** instance id missing ***")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        
        class_name = args[0]
        instance_id = args[1]
        attr_name = args[2]
        attr_value = args[3]


        if class_name not in globals():
            print(" *** class doesn't exist ***")
            return
            
        key = f'{class_name}.{instance_id}'

        if key not in storage.all():
            print(" ** no intance found **")

        # fetch the instance
        instance = storage.all()[key]

        # ensure id, created_at, and updated_at can't be updated
        if attr_name in ['id', 'created_at', 'updated_at']:
            print(f'** cannot update {attr_name} **')
            return
        
        # cast the attribute value to the approriate type
        if hasattr(instance, attr_name):
            current_value = getattr(instance, attr_name)
            attr_type = type(current_value)
            try:
                if attr_type == int:
                    attr_type = int(attr_type)
                elif attr_type == float:
                    attr_value = float(attr_value)
                elif attr_type == str:
                    attr_value = str(attr_value)
            except ValueError:
                print('** invalid value type **')
                return
        else:
            # If the attribute doesn't exist, assume string type
            attr_value = str(attr_value)

        # update the attribute and save the instance
        setattr(instance, attr_name, attr_value)
        instance.save()
        print('** attribute updated successfully!!! **')            


        

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