import cts.application.node
import cts.application.stringtable

class menudriver:
    """in charge of moving up and down the menu tree, executing the functions of external nodes where necessary"""
    def __init__(self, name, menu_list):
        """menu_list is a list of the 'first children' of the menu to be created"""
        self.name = name
        self.root_node = cts.application.node.rootnode(self.name, menu_list)
        self.current_node = self.root_node

    def Select(self, input):
        r=-1
        selection = self.current_node.Select(input)
        if selection:
            if selection.IsInterior():
                self.current_node = selection
                self.current_node.Refresh()
            elif selection.IsBack():
                self.current_node = selection.Select()
                self.current_node.Refresh()
            else:
                r = selection.Select()
        return r
            
    def JumpToTop(self):
        self.current_node = self.root_node
        
    def GetStringTable(self):
        return self.current_node.GetStringTable()
    
    