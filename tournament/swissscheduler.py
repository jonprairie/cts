from cts.options.header import *

class swissscheduler:
    """generates swiss rounds for a tournament schedule"""
    
    def __init__(self, rounds = default_options["tournament_rounds"]):
        
        self.rounds = rounds
        
    def GetNumRounds(self):
        return self.rounds
        
    def GenNextRoundSchedule(self):
        pass