class req:
    """class representing the requirements a player must meet in order to be considered for an invitation to a tournament"""
    
    def __init__(self, req_list):
        """req_list should be a list of strings in the form of a boolean test, all references to the player should use 'p'
        (for example: "p.GetCountry().GetName() is 'russia'" )"""
        
        self.req_list = req_list
        
    def setReqs(self, req_list):
        self.req_list = req_list
        
    def appendReq(self, req):
        self.req_list.append(req)
        
    def Test(self, p):
        for r in self.req_list:
            if not eval(r):
                return 0
        return 1