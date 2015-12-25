import linkedhandler
import cts.tournament.tournament as tournament
import cts.database.tournamentnameinterface
import cts.chess_federation.chessfederation


class tournamenthandler(linkedhandler.linkedhandler):
    """tournament handler, generates and maintains the tournament list for the game instance"""
    
    def __init__(self):
        self.old_tournament_list = []
        self.current_tournament_list = []
        self.waiting_tournament_list = []
        self.new_tournament_list = []
        
        self.player_handler = 0
        self.calendar_handler = 0        

    def GenInitialTournaments(self, day):
        self.new_tournament_list.append(tournament.tournament("Michigan Invitational", start_date = day, open = 0, tournament_type = "round robin", double_rr = 0))
        self.DailyMaintenance()
        self.WeeklyMaintenance()
   
    def GenTournament(self, day):
        """generates a randomly named tournament, the start date will be 7 days after the date it is created on"""
        """
        name = cts.database.tournamentnameinterface.GenRandTournamentName() +" " + str(self.calendar_handler.GetCurrentDate().GetDate())
        t = tournament.tournament(name, start_date = day, open = 0, tournament_type = "round robin", double_rr = 0)
        t.AddDateRange(self.calendar_handler.GetDateRange(t.GetStartDate(), t.GetDateIndexList()))
        self.new_tournament_list.append(t)
        """
        
    def CancelTournament(self, t):
        t.Cancel()
        if t in self.waiting_tournament_list:
            self.waiting_tournament_list.remove(t)
        elif t in self.current_tournament_list:
            self.current_tournament_list.remove(t)
        elif t in self.new_tournament_list:
            self.new_tournament_list.remove(t)
    
    #Get Functions
    def GetAllFutureTournaments(self):
        ret_list = self.new_tournament_list
        ret_list.extend(self.waiting_tournament_list)
        return ret_list
        
    def GetCurrentTournaments(self):
        return self.current_tournament_list
        
    def GetNewTournaments(self):
        return self.new_tournament_list
        
    def GetWaitingTournaments(self):
        return self.waiting_tournament_list
        
    def GetOldTournamentList(self):
        return self.old_tournament_list
        
    #Transfer Functions, move tournaments through the tournament lists: new -> waiting -> current -> old    
    def TransferToOld(self, t):
        """transfers a tournament from the current tournament list to the old tournament list once it's finished"""
        
        if t in self.current_tournament_list:
            self.current_tournament_list.remove(t)
            self.old_tournament_list.append(t)
        
    def TransferToCurrent(self, t):
        """transfers a tournament from the waiting tournament list to the current tournament list once it starts"""
        
        if t in self.waiting_tournament_list:
            self.waiting_tournament_list.remove(t)
            self.current_tournament_list.append(t)               
        
    def TransferToWaiting(self, t):
        """transfers a tournament from the new tournament list to the waiting tournament list after being fully initialized"""

        if t in self.new_tournament_list:
            self.new_tournament_list.remove(t)
            if not t in self.waiting_tournament_list:
                self.waiting_tournament_list.append(t)
     
    #Maintenance Functions
    def AddTournamentToDateRange(self, t):
        """takes a tournament and adds it to the dates on which the tournament is played"""
        
        date_list = self.calendar_handler.GetDateRange(t.GetStartDate(), t.GetDateIndexList())
        for day in date_list:
            day.AddTournament(t)   
    
    def NewTournamentMaintenance(self):
        """maintains the new tournament list"""
  
        for t in self.GetNewTournaments()[:]:                   #the '[:]' creates and returns a copy since it's not safe to modify the iterating list in the 'for' construct
            self.TransferToWaiting(t)
            t.AddDateRange(self.calendar_handler.GetDateRange(t.GetStartDate(), t.GetDateIndexList()))
            
    def WaitingTournamentMaintenance(self):
        """transfers 'waiting' tournaments to the current list once their start date is reached"""
        today = self.calendar_handler.GetCurrentDate()
        for t in self.GetWaitingTournaments()[:]:
            if ((t.GetStartDate() < today) or (t.GetStartDate() is today)):
                if t.IsReady():
                    t.TournamentInit()
                    t.AddDateRange(self.calendar_handler.GetDateRange(t.GetStartDate(), t.GetDateIndexList()))
                    self.AddTournamentToDateRange(t)
                    self.TransferToCurrent(t)
                else:
                    self.CancelTournament(t)
                    
    def CurrentTournamentMaintenance(self):
        """transfers 'current' tournaments to the old list once they've finished"""
        for t in self.GetCurrentTournaments()[:]:
            if t.IsFinished():
                self.TransferToOld(t)
                 
    def SendInvites(self):
        """Sends invites to players from 'Invitational' (non-open) tournaments"""

        player_list = self.player_handler.GetPlayers()
        for t in self.new_tournament_list:
            if not t.IsOpen():
                t.SendInvites(player_list)
    
    def MonthlyMaintenance(self):
        pass
    
    def WeeklyMaintenance(self):
        num_weekly_tournaments = int(self.player_handler.GetNumPlayers()/20)
        for t in range(num_weekly_tournaments):
            self.GenTournament(self.calendar_handler.GetDate(7))
        
    def TournamentNotInList(self, tournament):
        if tournament in self.GetAllFutureTournaments():
            return 0
        else:
            return 1
        
    def DailyMaintenance(self):
        for t in self.GetAllFutureTournaments():
            t.DailyMaintenance(self.player_handler.GetPlayers())
            
        self.NewTournamentMaintenance()
        self.WaitingTournamentMaintenance()
        self.CurrentTournamentMaintenance()