import cts.application.row

class selectableslot(cts.application.row.row):
    def __init__(self, key, slot_entry):
        self.key = key
        self.slot_entry = slot_entry
        cts.application.row.row.__init__(self, dict(key=self.key, name=self.slot_entry.GetName()))
    
    def GetDictTuple(self):
        return (self.key, self.slot_entry)
        
    def GetEntry(self):
        return self.slot_entry