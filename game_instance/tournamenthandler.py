import cts.tournament.tournament as tournament

class tournamenthandler:
    """tournament handler, generates and maintains the tournament list for the game instance"""
    
    def __init__(self):
        self.old_tournament_list = []
        self.current_tournament_list = []
        self.waiting_tournament_list = []
        self.new_tournament_list = []

    def GenInitialTournaments(self, date):
        self.new_tournament_list.append(tournament.tournament("Michigan Invitational", start_date = date, open = 0, tournament_type = "round robin", double_rr = 1))
    
    #Get Functions
    def GetCurrentTournaments(self):
        return self.current_tournament_list
        
    def GetNewTournaments(self):
        return self.new_tournament_list
        
    def GetWaitingTournaments(self):
        return self.waiting_tournament_list
        
    def GetOldTournamentList(self):
        return self.old_tournament_list
        
    #Transfer Functions    
    def TransferToOld(self, t):
        """transfers a tournament from the current tournament list to the old tournament list once it's finished"""
        
        if self.current_tournament_list.count(t):
            self.current_tournament_list.remove(t)
            self.old_tournament_list.append(t)
        
    def TransferToCurrent(self, t):
        """transfers a tournament from the waiting tournament list to the current tournament list once it starts"""
        
        if self.waiting_tournament_list.count(t):
            self.waiting_tournament_list.remove(t)
            self.current_tournament_list.append(t)               
        
    def TransferToWaiting(self, t):
        """transfers a tournament from the new tournament list to the waiting tournament list after being fully initialized"""
        
        if self.new_tournament_list.count(t):
            self.new_tournament_list.remove(t)
            self.waiting_tournament_list.append(t)
     
    #Maintenance Functions
    def NewTournamentMaintenance(self, date):
        """maintains the new tournament list"""
        
        for t in self.GetNewTournaments():
            self.TransferToWaiting(t)
            
    def WaitingTournamentMaintenance(self, date):
        """maintains the waiting tournament list"""
        
        transfers = []
        for t in self.GetWaitingTournaments():
            if t.GetStartDate() is date:
                if t.IsReady():
                    t.TournamentInit()
                    transfers.append(t)
                    self.TransferToCurrent(t)
        return transfers
                
    def CurrentTournamentMaintenance(self):
        """maintains the current tournament list"""
        
        for t in self.GetCurrentTournaments():
            if t.IsFinished():
                self.TransferToOld(t)
                 
    def SendInvites(self, player_list):
        """Sends invites to players from 'Invitational' (non-open) tournaments"""
        
        for t in self.new_tournament_list:
            if not t.IsOpen():
                t.SendInvites(player_list)
                
 