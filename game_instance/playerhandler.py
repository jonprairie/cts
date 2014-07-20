from cts.options.header import *
import cts.player.player as player

class playerhandler:
    """player handler, generates and maintains the player list for the game instance"""
    
    def __init__(self):
        self.player_list = []
       
    def InitPlayers(self):
        self.player_list.append(player.player("Magnus", "Carlsen", 23, elo_seed=2876.9))
        self.player_list.append(player.player("Levon", "Aronian", 30, elo_seed=2804.5))
        self.player_list.append(player.player("Hikaru", "Nakamura", 26, elo_seed=2787.2))
        self.player_list.append(player.player("Vladimir", "Kramnik", 38, elo_seed=2776.6))
        self.player_list.append(player.player("Vishwanathan", "Anand", 42, elo_seed=2785.0))
        self.player_list.append(player.player("Sergei", "Karjakin", 23, elo_seed=2786.4))
        self.player_list.append(player.player("Boris", "Gelfand", 43, elo_seed=2753.0))
        self.player_list.append(player.player("Anish", "Giri", 20, elo_seed=2750.0))
        self.player_list.append(player.player("Mickey", "Adams", 40, elo_seed=2743.0))
        self.player_list.append(player.player("Vesselin", "Topalov", 42, elo_seed=2772.4))
    
    #Get Functions
    def GetPlayers(self):
        return self.player_list
    
    #Maintenance Functions
    def RegisterForTournaments(self, tournament_list):
        for player in self.player_list:
            player.RegisterForTournaments(tournament_list)
            
def PlayerCMP(player_x, player_y):
    """returns 1 if player_x's elo is greater than player_y's elo, 0 if they are equal, and -1 otherwise"""
        
    if player_x.GetElo() > player_y.GetElo():
        return -1
    elif player_y.GetElo() > player_x.GetElo():
        return 1
    else:
        return 0
