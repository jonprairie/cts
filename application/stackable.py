from cts.options.header import *
import menu

class stackable:
    def __init__(self, menu_tree, name = ""):
        self.name = name
        self.menu_tree = menu_tree
        
        self.menu = menu.menu(self.menu_tree, self.name)
        self.is_exit = 0
        
    def IsExit(self):
        return self.is_exit
        
    def MakeExit(self):
        self.is_exit = 1
        
    def ResetExit(self):
        self.is_exit = 0
        
    def PassControl(self, to_stack):
        """takes a stackable object and puts it on the gamestack"""

        game_stack.Append(to_stack)
        
    def Loop(self):
        DisplayTable(self.menu.ToStringTable())
        inp = raw_input()
        self.menu.ChooseOption(inp)