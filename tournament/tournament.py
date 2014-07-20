from cts.options.header import *
import cts.application.stackable as stackable
import schedulehandler
import playerresultshandler

class tournament(stackable.stackable):
    """base class for tournaments"""
    
    def __init__(self, name, start_date = 0, rounds = default_options["tournament_rounds"], player_range = [], time_control = default_options["time_control"], open = 1, tournament_type = default_options["tournament_type"], double_rr = default_options["double_rr"], prestige = default_options["tournament_prestige"]):
        self.name = name                    #name of tournament        

        self.menu_list = [("back", [], self.MakeExit),
		                  ("play tournament", [], self.PlayTournament),
                          ("play round", [], self.PlayCurrentRound),
                          ("results", [], self.DisplayResults)]
                          
        stackable.stackable.__init__(self, self.menu_list, self.name)
        
        self.start_date = start_date
        self.rounds = rounds                #number of rounds in tournament
        self.time_control = time_control    #time control of games in tournament
        self.open = open                    #whether the tournament is open or closed (invite only)
        self.prestige = prestige            #prestige of tournament, used when sending invites to players
                                            #Not Implemented Yet
        
        self.player_list = []               #list of players

        self.schedule_handler = 0        
        self.player_result_handler = 0
        
        self.tournament_type = tournament_type            #type of tournament, 'round robin' or 'swiss'
        self.double_rr = double_rr                        #double round robin
        
        self.min_players, self.max_players = self.InitPlayerRange(player_range)
        
        self.is_initialized = 0
        self.current = 0
        
    def InitPlayerRange(self, player_range):
        if not player_range:
            if not cmp(self.tournament_type, "round robin"):
                return default_options["round_robin_player_range"]
            elif not cmp(self.tournament_type, "swiss"):
                return default_options["swiss_player_range"]
        else:
            return player_range
        
    def TournamentInit(self):
        """Initializes main components of the tournament. Should be called once tournament is full and ready to start"""
        
        if not self.is_initialized:
            self.is_initialized = 1
            player_list = self.GetPlayers()
            
            #creates a rr or swiss schedule handler, depending on the tournament's type
            if not cmp(self.tournament_type, "round robin"):
                self.schedule_handler = schedulehandler.rrschedulehandler(player_list, self.double_rr)
            elif not cmp(self.tournament_type, "swiss"):
                self.schedule_handler = schedulehandler.swissschedulehandler(player_list, self.rounds)
                
            self.player_result_handler = playerresultshandler.playerresultshandler(self, player_list)
            
            self.schedule_handler.GenSchedule()

    #Get Functions
    def GetPlayers(self):
        """returns list of players"""
        
        return self.player_list
        
    def GetStartDate(self):
        return self.start_date
        
    def GetNumRounds(self):
        return self.schedule_handler.GetNumRounds()

    def GetCurrentResults(self):
        """returns table of players and their overall results, sorted by score"""
        
        return self.player_result_handler.ToStringTable()
 
    #Test Functions    
    def IsInitialized(self):
        return self.is_initialized
        
    def IsFinished(self):
        return self.schedule_handler.IsFinished()
        
    def IsReady(self):
        if len(self.GetPlayers()) >= self.min_players:
            if len(self.GetPlayers()) <= self.max_players:
                return 1
        return 0
        
    def IsOpen(self):
        return self.open
        
    #Maintenance Functions
    def AddPlayer(self, player):
        """adds single player to tournament"""
        
        if len(self.player_list) < self.max_players:
            if not player in self.player_list:
                self.player_list.append(player)
                return 1
        return 0

    def AddPlayers(self, players):
        """adds a list of players to the tournament"""
        
        for new_player in players:
            self.AddPlayer(new_player)
            
    def SendInvites(self, players):
        """Takes a list of players and sends invites to certain ones"""
        
        #basic implementation, invites everyone
        for player in players:
            accept = player.EvaluateInvite(self)
            if accept:
                self.AddPlayer(player)

    #Play Functions            
    def PlayTournament(self):
        while not self.schedule_handler.IsFinished():
            self.PlayCurrentRound()
    
    def PlayCurrentRound(self):
        """plays the current round, then sends the results to the player result handler"""
        
        round_played = self.schedule_handler.PlayCurrentRound()
        if round_played:
            temp_results = self.schedule_handler.GetRoundResults()
            self.player_result_handler.AddRoundResults(temp_results)
            return 1
        else:
            return 0
   
    #Player Interface/Menu Functions
    def DisplayResults(self):
        DisplayTable(self.ToStringTable())
        
    #String Functions            
    def StringTHeader(self):
        """returns a header for the tournament in string form"""
        
        strth = self.name.upper()
        strth += "\n"
        strth += "Players: "                        
        strth += str(len(self.GetPlayers()))
        strth += "\n"
        strth += "Rounds: "
        strth += str(self.schedule_handler.GetNumRounds())
        strth += "\n"
        strth += "Type: "
        strth += self.tournament_type
        strth += "\n"
        
        return strth
        
    def ToStringTable(self):
        header_row = ["header", self.StringTHeader()]
        ret_table = self.GetCurrentResults()
        ret_table.insert(0, header_row)
        return ret_table