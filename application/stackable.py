from cts.options.header import *
import cts.application.menudriver
import menu

class stackable:
    def __init__(self, menu_list, name = ""):
        self.name = name
        self.menu_list = menu_list
        
        self.header = ""
        
        self.menu = cts.application.menudriver.menudriver(self.name, self.menu_list)
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
        if self.header:
            Display(self.header)
        DisplayStringTable(self.menu.GetStringTable())
        inp = raw_input()
        self.menu.Select(inp)