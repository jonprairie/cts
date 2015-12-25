class numgenerator:
    def __init__(self):
        self.num = 0
        
    def GenNum(self):
        self.num += 1
        return self.num - 1
        
num_gen = numgenerator()