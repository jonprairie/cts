class gamestack:    
    def __init__(self):
        self.contents = []
        self.last = -1
        
    def Append(self, toappend):
        self.contents.append(toappend)
        self.last += 1
        
    def Pop(self):
        toreturn = self.contents[self.last]
        self.contents.pop()
        self.last -= 1
        return toreturn
        
    def Peek(self):
        return self.contents[self.last]
        
    def IsEmpty(self):
        return (self.last is -1)
        
    def PeekLoop(self):
        self.Peek().Loop()
        
    def PeekIsExit(self):
        return self.Peek().IsExit()