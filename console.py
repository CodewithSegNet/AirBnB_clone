#!/usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):
    """ A console that contains the entry point of the command interpreter """
    prompt = '(hbnb)'


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