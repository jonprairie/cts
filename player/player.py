from cts.options.header import *
import cts.application.row
import playertournamenthandler
import cts.player.numgenerator

class player(cts.application.row.row):
    """chess player"""
    
    def __init__(self, first_name, last_name, age, gender = "male", country=0, title = None, elo = default_options["elo"], play_strength = 0, fame = default_options["player_fame"], player_type = "cpu"):
        
        self.player_num = cts.player.numgenerator.num_gen.GenNum()
        self.first_name = first_name    #player's first name
        self.last_name = last_name      #player's last name
        self.age = age                  #player's age
        self.gender = gender
        self.country = country
        self.title = title              #player's title
        self.elo = float(elo)           #player's elo
        self.live_elo = float(elo)
        self.chess_federation = 0
        self.play_strength = play_strength
            
        self.player_type = player_type   #computer, human, bye
        
        self.tournament_invites = []
        self.player_tournament_handler = playertournamenthandler.playertournamenthandler()
        
        cts.application.row.row.__init__(self, dict(last=self.last_name, first=self.first_name, age=self.age, country=self.country.GetShortName(), elo=self.elo))
        
    #Get Functions
    def GetPlayerNum(self):
        return self.player_num
        
    def GetType(self):
        return self.player_type
        
    def GetName(self, invert=0):
        name = ""
        if invert:
            name = self.last_name + ", " + self.first_name
        else:
            name = self.first_name + " " + self.last_name
            
        return name
        
    def GetGender(self):
        return self.gender
        
    def GetCountry(self):
        return self.country
        
    def GetElo(self):
        """returns official elo"""
        
        return self.elo 
        
    def GetLiveElo(self):
        """returns 'live' elo"""
        return self.live_elo
       
    def GetPlayStrength(self):
        return self.play_strength.GetPlayStrength()
        
    def NameLength(self):
        """returns length of string returned by InvertName()"""
    
        return len(self.InvertName())

    def InvertName(self):
        """returns player's full name in "last, first" form"""
        
        name = self.last_name + ", " + self.first_name
        return name        
    
    #Maintenance Functions
    def MonthlyMaintenance(self):
        self.UpdateElo()
        
    def WeeklyMaintenance(self):
        pass

    def DailyMaintenance(self):
        self.ProcessTournamentInvites()
        self.player_tournament_handler.TransferToOld()
        self.player_tournament_handler.TransferToCurrent()
        
    def SetFederation(self, chess_federation):
        self.chess_federation = chess_federation
        
    def ProcessTournamentInvites(self):
        for invite in self.tournament_invites:
            if self.EvaluateInvite(invite.GetInviter()):
                invite.Accept()
            else:
                invite.Decline()
        
    def CancelTournament(self, t):
        self.player_tournament_handler.CancelTournament(t)
     
    def AddGame(self, game):
        if not game in self.player_tournament_handler.GetGameList():
            self.player_tournament_handler.AddGame(game)
            
    def AddTournamentInvite(self, invite):
        self.tournament_invites.append(invite)
        
    def UpdateElo(self, rating_adjustment):
        self.elo = self.live_elo

    def UpdateLiveElo(self, rating_adjustment):
        self.live_elo += rating_adjustment
        
    def EvaluateInvite(self, tournament):
        """Evaluates an invitation from a tournament. Accepts or rejects the invite.
        If the player accepts the invite, adds the tournament to the player's tournament
        list"""
        
        #For now it's a basic implementation that accepts most invites
        if not self.player_tournament_handler.TournamentConflicts(tournament):
            return 1
        else:
            return 0
            
    def RegisterForTournaments(self, tournaments):
        """Takes a list of tournaments and chooses which of them to register for"""
        
        #Basic Implementation
        for t in tournaments:
            if t.IsOpen():
                if not self.player_tournament_handler.TournamentConflicts(t):
                    t.AddPlayer(self)
                    
                    
#Deprecated                    
class bye(player):
    def __init__(self):
        player.__init__(self, "bye", "bye", 0, ptype="bye")
        
    def GetName(self, invert=0):
        return "bye"