class playerhistoryhandler:
    def __init__(self):
        self.old_tournament_list = []
        self.current_tournament = 0
        self.future_tournament_list = []
        
        self.tournament_history = []
        self.game_list = []
        
    #Get Functions
    def GetOldTournaments(self):
        temp_list = []
        temp_list.extend(self.old_tournament_list)
        return temp_list
        
    def GetCurrentTournament(self):
        return self.current_tournament
        
    def GetFutureTournaments(self):
        temp_list = []
        temp_list.extend(self.future_tournament_list)
        return temp_list
        
    def GetTournamentHistory(self):
        temp_list = []
        temp_list.extend(self.tournament_history)
        return temp_list
        
    def GetGameList(self):
        temp_list = []
        temp_list.extend(self.game_list)
        return temp_list
        
    #Add Functions
    def AddNewTournament(self, tournament):
        if not tournament in self.future_tournament_list:
            self.future_tournament_list.append(tournament)
            
    def AddGame(self, game):
        if game not in self.game_list:
            self.game_list.append(game)
            return 1
        return 0
    
    #Transfer Functions
    def TransferToCurrent(self):
        for t in self.future_tournament_list:
            if t.IsCurrent():
                self.current_tournament = t
                self.future_tournament_list.remove(t)
                
    def TransferToOld(self):
        if self.current_tournament.IsFinished():
            self.old_tournament_list.append(self.current_tournament)
            self.current_tournament = 0
            
            