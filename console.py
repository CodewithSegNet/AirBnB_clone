#!/usr/bin/python3

"""
    command line program
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    command line interpreter
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """ a command that exits the interpreter """
        print('Exiting program')
        return True

    def help_quit(self):
        """ a command that exits the interpreter"""
        print('Quit command to exit the program')
        print('usage: quit')

    def do_EOF(self, line):
        """ a command that exits the interpreter """
        print('Exiting program')
        return True

    def help_EOF(self):
        """ a command that exits the interpreter"""
        print('Quit command to exit the program')
        print('usage: ctrl+d')

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
