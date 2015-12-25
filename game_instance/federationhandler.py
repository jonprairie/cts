import linkedhandler
import cts.tournament.tournament
import random

class federationhandler(linkedhandler.linkedhandler):
    def __init__(self):
        self.tcf = cts.chess_federation.chessfederation.parentfederation()          #terran chess federation

    def PullTournaments(self):
        temp_tourn_list1 = self.tcf.PullChildrenTournaments()
        temp_tourn_list2 = []
        if temp_tourn_list1:
            for t in temp_tourn_list1:
                if not t in self.tournament_handler.GetAllFutureTournaments():
                    t.AddStartDate(self.calendar_handler.GetDate(t.GetStartDate()))
                    temp_tourn_list2.append(t)
            self.tournament_handler.new_tournament_list.extend(temp_tourn_list2)

    def RegisterPlayers(self):
        """place players in the appropriate federation"""
        self.tcf.RegisterPlayers(self.player_handler.GetPlayers())
    
    def DailyMaintenance(self):
        self.PullTournaments()
        
    def WeeklyMaintenance(self):
        pass
        
    def MonthlyMaintenance(self):
        pass
        
