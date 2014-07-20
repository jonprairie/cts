from cts.options.header import *
import playerhistoryhandler

class player:
    """chess player"""
    
    def __init__(self, first_name, last_name, age, title = None, elo_dict = default_options["elo_dict"], elo_seed = 0, fame = default_options["player_fame"], player_type = "computer"):
        
        self.first_name = first_name    #player's first name
        self.last_name = last_name      #player's last name
        self.age = age                  #player's age
        self.title = title              #player's title
        self.elo_dict = elo_dict        #dictionary of a player's elo, telo (true elo), topelo (true opening elo),
                                        #tmgelo (true middlegame elo), tenelo (true endgame elo), and lelo (live elo)
        
        if elo_seed:
            self.ExpandEloSeed(elo_seed)
            
        self.player_type = player_type   #computer, human, bye
        
        self.player_history_handler = playerhistoryhandler.playerhistoryhandler()
        
    #Get Functions
    def GetType(self):
        return self.player_type
        
    def GetName(self, invert=0):
        name = ""
        if invert:
            name = self.last_name + ", " + self.first_name
        else:
            name = self.first_name + " " + self.last_name
            
        return name
        
    def GetElo(self, key="elo"):
        """returns value in elodict corresponding to the key"""
        
        return float(self.elo_dict[key]) 
        
    def NameLength(self):
        """returns length of string returned by InvertName()"""
    
        return len(self.InvertName())

    def InvertName(self):
        """returns player's full name in "last, first" form"""
        
        name = self.last_name + ", " + self.first_name
        return name        
    
    #Maintenance Functions
    def DailyMaintenance(self):
        self.player_history_handler.TransferToOld()
        self.player_history_handler.TransferToCurrent()
        
    def MonthlyMaintenance(self):
        self.elo_dict["elo"] = self.elo_dict["lelo"]
    
    def ExpandEloSeed(self, elo_seed):
        self.elo_dict = dict(elo=elo_seed, telo=elo_seed, topelo=elo_seed, tmgelo=elo_seed, tenelo=elo_seed, lelo=elo_seed)
        
    def AddGame(self, game):
        if not game in self.player_history_handler.GetGameList():
            self.player_history_handler.AddGame(game)
        
    def UpdateElo(self, rating_adjustment):
        self.elo_dict["lelo"] += rating_adjustment
        
    def EvaluateInvite(self, tournament):
        """Evaluates an invitation from a tournament. Accepts or rejects the invite.
        If the player accepts the invite, adds the tournament to the player's tournament
        list"""
        
        #For now it's a basic implementation that accepts all invites
        self.player_history_handler.AddNewTournament(tournament)
        return 1
            
    def RegisterForTournaments(self, tournaments):
        """Takes a list of tournaments and chooses which of them to register for"""
        
        #Basic Implementation
        for t in tournaments:
            if t.IsOpen():
                if t.AddPlayer(self):
                    self.player_history_handler.AddNewTournament(t)
        
class bye(player):
    def __init__(self):
        player.__init__(self, "bye", "bye", 0, ptype="bye")
        
    def GetName(self, invert=0):
        return "bye"