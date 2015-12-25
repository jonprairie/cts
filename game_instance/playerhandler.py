import linkedhandler
from cts.options.header import *
import cts.player.player as player
import cts.stat_res.genplayer as genplayer

class playerhandler(linkedhandler.linkedhandler):
    """player handler, generates and maintains the player list for the game instance"""
    
    def __init__(self):
        self.player_list = []
        
        self.calendar_handler = 0
        self.tournament_handler = 0
        self.num_players = default_options["num_initial_cpu_players"]

    def InitPlayers(self):
        for p in range(self.num_players):
            self.GenPlayer()
        
    def GenPlayer(self):
        new_player = genplayer.GenPlayer()
        self.player_list.append(new_player)
        
    def GetNumPlayers(self):
        return self.num_players
    
    #Get Functions
    def GetPlayers(self):
        return self.player_list
    
    #Maintenance Functions
    def RegisterForTournaments(self):
        tournament_list = self.tournament_handler.GetNewTournaments()
        for p in self.player_list:
            p.RegisterForTournaments(tournament_list)
           
    def MonthlyMaintenance(self):
        for p in self.player_list: 
            p.MonthlyMaintenance()           
           
    def WeeklyMaintenance(self):        
        for p in self.player_list: 
            p.WeeklyMaintenance()
            
    def DailyMaintenance(self):
        self.RegisterForTournaments()

        for p in self.player_list: 
            p.DailyMaintenance()
            
def PlayerCMP(player_x, player_y):
    """returns -1 if player_x's elo is greater than player_y's elo, 0 if they are equal, and 1 otherwise"""
        
    if player_x.GetElo() > player_y.GetElo():
        return -1
    elif player_y.GetElo() > player_x.GetElo():
        return 1
    else:
        return 0
