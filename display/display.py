def DisplayTable(string_table, horizontal_padding = 3):
    """Takes a table of strings and displays it"""
    
    disp_str = ""
    horizontal_pad = ""
    for buff in range(horizontal_padding):
        horizontal_pad += " "
            
    collumn_width = []
    
    if not cmp(string_table[0][0], "header"):
        Display(string_table[0][1])
        string_table.remove(string_table[0])
    
    max_row_length = 0
    for row in string_table:
        if len(row) > max_row_length:
            max_row_length = len(row)
    for num in range(max_row_length):
        collumn_width.append(1)
        
    for row in string_table:
        for collumn_index in range(len(row)):
            if len(row[collumn_index]) > collumn_width[collumn_index]:
                collumn_width[collumn_index] = len(row[collumn_index])
                
    for row in string_table:
        for collumn_index in range(len(row)):
            disp_str += row[collumn_index].ljust(collumn_width[collumn_index])
            disp_str += horizontal_pad
        disp_str += "\n"
           
    Display(disp_str)
    
def Display(string):
    print string