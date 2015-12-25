def RowCMPGenerator(key):
    def RowCMP(x,y):
        return cmp(x.GetValue(key), y.GetValue(key))
    return RowCMP
 
class stringtable:
    """Must be made up of row instance variables of the same type"""
    def __init__(self, header, rows, def_key=None, show_keys=1):
        self.header = header
        self.row_keys = []
        if rows:
            self.row_keys = rows[0].GetKeys()
        self.rows = rows
        self.def_key = def_key
        self.show_keys=show_keys
        
    def __str__(self):
        return self.ToString()
        
    def SortBy(self, k, ascending=1):
        if not k:
            k = self.def_key
        sort_key = k
        self.rows.sort(cmp=RowCMPGenerator(sort_key), reverse = not ascending)
       
    def GetRowKeys(self):
        return self.row_keys
        
    def ReplaceRows(self, new_rows):
        self.rows = new_rows
        if self.rows:
            self.row_keys = self.rows[0].GetKeys()
        
    def BuildMaxCollumns(self):
        dict_list = []
        for k in self.row_keys:
            temp_tuple = 0
            if self.show_keys:
                temp_tuple = (k, len(str(k)))
            else:
                temp_tuple = (k, 0)
            dict_list.append(temp_tuple)
        ret_dict = dict(dict_list)
        return ret_dict
        
    def GetStringTable(self):
        """Builds a table of strings out of the stringtable"""
        ret_table = []
        for r in self.rows:
            temp_dict = r.ToStringDict()
            ret_table.append(temp_dict)
        return ret_table
        
    def CollumnWidthCMP(self, max_collumns, new_row):
        """takes a row of the lengths of the longest entries in each collumn of a table, compares it
           to a new row and updates the first if necessary, then returns it"""
        ret_list = []
        new_row_widths = new_row.GetCollumnWidths()
        for k in new_row.GetKeys():
            if new_row_widths[k] > max_collumns[k]:
                max_collumns[k] = new_row_widths[k]
        return max_collumns
        
    def GetMaxCollumnWidths(self):
        max_collumns = self.BuildMaxCollumns()
        for row in self.rows:
            max_collumns = self.CollumnWidthCMP(max_collumns, row)
        return max_collumns
        
    def ToString(self, horizontal_padding=3):
        """returns a string representation of the stringtable"""
        
        disp_str = ""
        horizontal_pad = ""
        for buff in range(horizontal_padding):
            horizontal_pad += " "
            
        collumn_widths = self.GetMaxCollumnWidths()
        table = self.GetStringTable()
        
        disp_str+=self.header.upper() + '\n'
        
        row_keys = self.GetRowKeys()
        if self.show_keys:
            for k in row_keys:
                disp_str+=str(k).ljust(collumn_widths[k]).upper()
                disp_str+=horizontal_pad
            disp_str+="\n"
        
        for row in table:
            for k in row_keys:
                disp_str+=row[k].ljust(collumn_widths[k])
                disp_str+=horizontal_pad
            disp_str+="\n"
            
        return disp_str