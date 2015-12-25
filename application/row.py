class row:
    def __init__(self, collumn_dict):
        self.collumn_dict = collumn_dict
        self.default_switch_dict = dict.fromkeys(self.collumn_dict, 1)

    def UpdateRow(self, key, new_value):
        self.collumn_dict[key] = new_value
        
    def GetValue(self, key):
        return self.collumn_dict[key]
    
    def CheckSD(self, switch_dict):
        if not switch_dict:
            switch_dict = self.default_switch_dict
        return switch_dict
        
    def ToStringDict(self, switch_dict = 0):
        switch_dict = self.CheckSD(switch_dict)
        dict_list = []
        for k in self.GetKeys():
            if switch_dict[k]:
                temp_tuple = (k, str(self.collumn_dict[k]))
                dict_list.append(temp_tuple)
        ret_dict = dict(dict_list)
        return ret_dict
        
    def GetLength(self):
        return len(self.collumn_dict)

    def GetCollumnWidths(self, switch_dict = 0):
        switch_dict = self.CheckSD(switch_dict)
        dict_list = []
        for k in self.GetKeys():
            if switch_dict[k]:
                temp_tuple = (k, len(str(self.collumn_dict[k])))
                dict_list.append(temp_tuple)
        ret_dict = dict(dict_list)
        return ret_dict        
    
    def GetKeys(self):
        return self.collumn_dict.keys()