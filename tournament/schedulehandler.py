from cts.options.header import *
import rrscheduler
import swissscheduler

class schedulehandler:
    """schedule handler, generates and maintains the play schedule for a tournament"""
    
    def __init__(self, player_list = [], tournament_type = default_options["tournament_type"], rounds = default_options["tournament_rounds"], double_rr = default_options["double_rr"]):
        
        self.player_list = player_list
        
        self.tournament_type = tournament_type
        self.double_rr = double_rr
        
        self.rounds = rounds
        self.current_round_index = 0
        self.current_round = 1
        
        self.last_round_results = 0
        
        self.scheduler = 0
        
        self.schedule = []
        self.is_finished = 0
        self.is_current = 0
        
    def GetNumRounds(self):
        return self.scheduler.GetNumRounds()
        
    def GetRoundResults(self):
        return self.last_round_results.GetGames()
        
    def GetSchedule(self):
        return self.schedule
        
    def IsFinished(self):
        return self.is_finished
        
    def IsCurrent(self):
        return self.is_current

    def GenSchedule(self):
        pass
        
    def PlayCurrentRound(self):
        pass
    
    def SetIfFinished(self):
        pass
     
    def SetCurrent(self):
        self.is_current = 1
        
class rrschedulehandler(schedulehandler):
    """generates and maintains the schedule for a round robin tournament"""
    
    def __init__(self, player_list = [], double_rr = default_options["double_rr"]):
        schedulehandler.__init__(self, player_list, "round robin", double_rr=double_rr)
        
        self.scheduler = rrscheduler.rrscheduler(double_rr = self.double_rr)
    
    def GenSchedule(self):
        self.schedule.extend(self.scheduler.GenSchedule(self.player_list))

    def PlayCurrentRound(self):
        if not self.IsFinished():
            if not self.is_current:
                self.is_current = 1
            self.schedule[self.current_round_index].PlayRound()
            self.last_round_results = self.schedule[self.current_round_index]
            
            self.current_round_index += 1
            self.current_round += 1
            
            self.SetIfFinished()
            return 1
        else:
            return 0
        
    def SetIfFinished(self):
        if self.current_round > self.scheduler.GetNumRounds():
            self.is_finished = 1
            self.is_current = 0
            
class swissschedulehandler(schedulehandler):
    """generates and maintains the schedule for a swiss tournament"""
    
    def __init__(self, player_list, rounds = default_options["tournament_rounds"]):
        schedulehandler.__init__(self, player_list, "swiss", rounds=rounds)
        
        self.scheduler = swissscheduler.swissscheduler(self.rounds)
        
    def GenSchedule(self):
        self.schedule.extend(self.scheduler.GenNextRoundSchedule())

        