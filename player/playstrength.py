class playstrength:
    def __init__(self, age, strength, strength_graph = []):
        self.age = age
        self.months = 0
        self.strength = strength
        self.strength_graph = strength_graph
        
    def GetPlayStrength(self):
        return self.strength
        
    def MonthlyMaintenance(self):
        self.months = (self.months + 1) % 12
        if not self.months:
            self.age += 1
        