import cts.application.stringtable
import cts.application.selectableslot

class selectablestringtable(cts.application.stringtable.stringtable):
    def __init__(self, header, rows, def_key=None, dynamic=0):
        self.dynamic = dynamic
        self.source_list = rows
        
        self.selectable_rows = []
        self.children_dict = []        
        self.BuildRows()
        
        cts.application.stringtable.stringtable.__init__(self, header, self.selectable_rows, def_key)
        
    def BuildRows(self):
        len_source = range(len(self.source_list))
        for r,n in zip(self.source_list, len_source):
            temp_el=cts.application.selectableslot.selectableslot.__init__(n, r.GetMenuElement())
            self.selectable_rows.append(temp_el)
        self.children_dict = dict([r.GetDictTuple() for r in self.selectable_rows])
        
    def Refresh(self):
        if dynamic:
            self.selectable_rows=[]
            self.children_dict = []
            self.BuildRows()
            
    def Select(self, key):
        if self.children_dict.has_key(key):
            return self.children_dict[key].Select()