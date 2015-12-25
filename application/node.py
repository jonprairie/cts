import cts.application.row
import cts.application.stringtable
import cts.application.selectableslot

class interiornode(cts.application.row.row):
    def __init__(self, header, children, parent=0, dynamic=0, children_func=0, make_back=1):
        """children_func is a function to call to get an updated list of children. Should only be used if dynamic==1"""
        
        self.header = header
        self.dynamic = dynamic
        self.children_func = children_func
        self.source_list = children
        if parent:
            self.parent = parent
        else:
            self.parent = self
        
        self.selectable_rows = []
        self.children_dict = []      
      
        self.make_back = make_back
        if self.make_back:
            self.back = cts.application.selectableslot.selectableslot("0", backnode(self.parent))
        
        self.BuildRows()      
        
        self.display_table = cts.application.stringtable.stringtable(header, self.selectable_rows, def_key="key", show_keys=0)
        cts.application.row.row.__init__(self, dict(name = header))
        
    def UpdateParent(self, new_parent):
        self.parent = new_parent
        self.back.GetEntry().UpdateParent(new_parent)
        
    def GetParent(self):
        return self.parent
        
    def GetStringTable(self):
        return self.display_table
        
    def GetName(self):
        return self.header
        
    def IsInterior(self):
        return 1
        
    def BuildRows(self):
        len_source = range(1, len(self.source_list)+1)
        for r,n in zip(self.source_list, len_source):
            temp_el=cts.application.selectableslot.selectableslot(str(n), r.GetMenuElement())
            temp_el.GetEntry().UpdateParent(self)
            self.selectable_rows.append(temp_el)
        if self.make_back:
            self.selectable_rows.append(self.back)
        self.children_dict = dict([r.GetDictTuple() for r in self.selectable_rows])
        
    def Refresh(self):
        if self.dynamic:
            self.selectable_rows=[]
            self.children_dict = []
            self.source_list = self.children_func()
            self.BuildRows()
            self.display_table.ReplaceRows(self.selectable_rows)
            
    def Select(self, key):
        if self.children_dict.has_key(key):
            return self.children_dict[key]
        else:
            return 0
            
    def GetMenuElement(self):
        return self

class exteriornode(cts.application.row.row):
    def __init__(self, header, action):
        self.header = header
        cts.application.row.row.__init__(self, dict(name = self.header))
        self.action = action
        
    def Select(self):
        return self.action()
        
    def GetName(self):
        return self.header        
    
    def IsInterior(self):
        return 0
        
    def IsBack(self):
        return 0
        
    def GetMenuElement(self):
        """a finesse function to make interiornode.BuildRows work when an exteriornode is passed as a child"""
        return self
        
    def UpdateParent(self, dummy_parent):
        """another finesse function to make interiornode.BuildRows work when updating the parent of children nodes"""
        pass
        
class backnode(cts.application.row.row):
    def __init__(self, parent):
        cts.application.row.row.__init__(self, dict(name = "back"))
        self.parent = parent
        
    def Select(self):
        return self.parent
        
    def UpdateParent(self, parent):
        self.parent = parent
    
    def GetName(self):
        return "back"
    
    def IsInterior(self):
        return 0
        
    def IsBack(self):
        return 1
        
class rootnode(interiornode):
    def __init__(self, header, children, dynamic=0):
        interiornode.__init__(self, header, children, 0, dynamic=dynamic, make_back=0)
