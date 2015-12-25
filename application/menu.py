import menuelement

class menu:
    def __init__(self, menu_tree, menu_name="parent"):
        self.menu_parent = menuelement.menuelement(menu_name,menu_tree,0,no_back=1)
        self.menu_stack = [self.menu_parent]
        self.current_element = self.menu_parent
        self.last_index = 0
        
    def ChooseOption(self, key):
        """takes a key and selects the child corresponding to that key in self.current_element.child_dict.
        if the child is a leaf node then its action function is called and self.current_element is left alone.
        Otherwise the selected child replaces self.current_element."""
        
        temp_element = self.current_element.GetChild(key)
        if temp_element:
            if temp_element.IsLeaf():
                temp_element.Action()
            elif temp_element.HasChildren():
                self.ClimbTree(temp_element)
            
            if self.current_element.IsExit():
                self.current_element.ResetExit()
                self.Back()
                
    def ClimbTree(self, menu_element):
        self.menu_stack.append(menu_element)
        self.UpdateCurrentElement(1)
        
    def UpdateCurrentElement(self, inc = 0):
        self.last_index += inc
        self.current_element = self.menu_stack[self.last_index]
        
    def Back(self):
        if self.last_index:
            self.menu_stack.pop()
            self.UpdateCurrentElement(-1)
        
    def ToStringTable(self):
        ret_table = []
        child_dict = self.current_element.GetChildDict()
        child_keys = child_dict.keys()
        child_keys.sort()
        
        header_row = ["header", self.current_element.ToString().upper() + ":"]
        ret_table.append(header_row)
        
        for key in child_keys:
            temp_row = []
            temp_row.append(" \"" + key + "\"")
            temp_row.append("---")
            temp_row.append(child_dict[key].ToString())
            ret_table.append(temp_row)
        
        return ret_table