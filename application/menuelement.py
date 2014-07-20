keys = "abcdefghijklmnopqrstuvwxyz1234567890"

class menuelement:
    def __init__(self, name, menu_tree, action, no_back = 0):
        self.name = name

        self.menu_tree = menu_tree
        self.children = []
        
        self.action = action
        self.is_leaf = 1
        
        self.is_exit = 0
        
        if self.menu_tree and not self.action:
            self.is_leaf = 0
            
        if not self.IsLeaf() and not no_back:
            self.menu_tree.insert(0,("back", [], self.MakeExit))
            
        for child,index in zip(self.menu_tree, range(len(self.menu_tree))):
            temp_child = menuelement(child[0],child[1],child[2])
            self.children.append(temp_child)
        
        if self.children:
            self.child_dict = dict(zip(keys, self.children))
            
    def IsLeaf(self):
        return self.is_leaf
        
    def IsExit(self):
        return self.is_exit
        
    def MakeExit(self):
        self.is_exit = 1
        
    def ResetExit(self):
        self.is_exit = 0
        
    def GetName(self):
        return self.name
        
    def GetChildDict(self):
        return self.child_dict
        
    def HasChildren(self):
        if self.children:
            return 1
        else:
            return 0
            
    def GetChildren(self):
        return self.children
        
    def GetChild(self, key):
        if self.child_dict.has_key(key):
            return self.child_dict[key]
        return 0
            
    def Action(self):
        if self.action:
            self.action()

    def ToString(self):
        return self.name
            
    def ChildrenToStringTable(self):
        ret_table = []
        for child in self.children:
            temp_table = child.ToStringTable()
            ret_table.append(temp_table)
        return ret_table
            
