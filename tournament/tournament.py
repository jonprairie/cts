from cts.options.header import *
import cts.application.stackable as stackable
import cts.application.stringtable
import cts.application.row
import cts.application.node
import cts.tournament.invitation
import cts.tournament.req
import schedulehandler
import playerresultshandler
import random

class tournament(stackable.stackable, cts.application.row.row):
    """base class for tournaments,
        I really need to refactor this class into a more polymorphic solution. I should have a basic tournament class with subclasses
        like a NationalChampionship, Candidates, WorldChampionshipMatch etc"""
    
    def __init__(self, name, player_range=[], start_date = 0, rounds = default_options["tournament_rounds"], time_control = default_options["time_control"], open = 1, tournament_type = default_options["tournament_type"], double_rr = default_options["double_rr"], prestige = default_options["tournament_prestige"]):
        self.name = name                    #name of tournament        

        self.menu_list = self.BuildMenu()
                          
        stackable.stackable.__init__(self, self.menu_list, self.name)
        
        self.start_date = start_date
        self.rounds = rounds                #number of rounds in tournament
        self.time_control = time_control    #time control of games in tournament
        self.open = open                    #whether the tournament is open or closed (invite only)
        self.prestige = prestige            #prestige of tournament, used when sending invites to players
                                            #Not Implemented Yet
        
        self.player_list = []               #list of players
        self.num_players = 0
        
        self.sent_invites = []
        self.players_invited = []           #dict of players that have been invited already
        self.sent_invites_st = cts.application.stringtable.stringtable("sent invites", self.sent_invites)

        self.schedule_handler = 0        
        self.player_result_handler = 0
        
        self.tournament_type = tournament_type            #type of tournament, 'round robin' or 'swiss'
        self.double_rr = double_rr                        #double round robin
        
        self.min_players, self.max_players = self.InitPlayerRange(player_range)
        self.player_requirements = cts.tournament.req.req([])
        
        self.date_index_list = self.SetDateIndexList(self.rounds, self.max_players)
        self.date_range = []
        
        self.is_initialized = 0
        self.is_current = 0
        
        self.results_st = 0
        self.player_st = cts.application.stringtable.stringtable(self.name+" Players:", self.player_list)
        cts.application.row.row.__init__(self, dict(name=self.name, type=self.tournament_type, rounds=self.rounds, players=self.num_players, date = self.start_date))
        
    def BuildMenu(self):
        en1 = cts.application.node.exteriornode("back", self.MakeExit)
        en2 = cts.application.node.exteriornode("play tournament", self.PlayTournament)
        en3 = cts.application.node.exteriornode("play round", self.PlayCurrentRound)
        en4 = cts.application.node.exteriornode("results", self.DisplayResults)
        en5 = cts.application.node.exteriornode("overview", self.ViewGeneral)
        en6 = cts.application.node.exteriornode("sent invites", self.ViewSentInvites)
        self.menu_element = cts.application.node.interiornode(self.name, [en5, en6])
        return [en1, en2, en3, en4]
        
    def InitPlayerRange(self, player_range):
        if not player_range:
            if not cmp(self.tournament_type, "round robin"):
                return default_options["round_robin_player_range"]
            elif not cmp(self.tournament_type, "swiss"):
                return default_options["swiss_player_range"]
        else:
            return player_range
        
    def SetDateIndexList(self, rounds, num_players):
        ret_list = []
        if not cmp(self.tournament_type, "round robin"):
            if not num_players % 2:
                ret_list = range(2*(num_players - 1) + default_options["tournament_rest_days"])
            else:
                ret_list = range(2*(num_players - 1))
        elif not cmp(self.tournament_type, "swiss"):
            ret_list = range(rounds)
        return ret_list
        
    def TournamentInit(self):
        """Initializes main components of the tournament. Should be called once tournament is full and ready to start"""
        
        if not self.is_initialized:
            self.is_initialized = 1
            self.is_current = 1
            player_list = self.GetPlayers()
            
            #creates a rr or swiss schedule handler, depending on the tournament's type
            if not cmp(self.tournament_type, "round robin"):
                self.schedule_handler = schedulehandler.rrschedulehandler(player_list, self.double_rr)
            elif not cmp(self.tournament_type, "swiss"):
                self.schedule_handler = schedulehandler.swissschedulehandler(player_list, self.rounds)
                
            self.player_result_handler = playerresultshandler.playerresultshandler(self, player_list)
            self.results_st = cts.application.stringtable.stringtable(self.name+" results", self.player_result_handler.GetList())
            
            self.schedule_handler.GenSchedule()
            self.date_index_list = range(self.GetNumRounds())

    def Cancel(self):
        for p in self.player_list:
            p.CancelTournament(self)
        for d in self.date_range:
            d.RemoveTournament(self)
            
    #Set Functions
    def SetPlayerRequirements(self, reqs):
        """reqs should be a list of strings which represent boolean tests that each player of the tournament has to pass.
        References to the player should use the variable p. For Example: "p.getCountry().getName() is 'russia'" """
            
        self.player_requirements.setReqs(reqs)
       
    def AddPlayerRequirement(self, req):
        self.player_requirements.appendReq(req)
        
    #Get Functions
    def GetMenuElement(self):
        return self.menu_element
        
    def GetName(self):
        return self.name
        
    def GetPlayers(self):
        """returns list of players"""
        
        return self.player_list
        
    def GetNumPlayers(self):
        return len(self.player_list)
        
    def GetStartDate(self):
        return self.start_date
        
    def GetNumRounds(self):
        return self.schedule_handler.GetNumRounds()

    def GetCurrentResults(self):
        """returns table of players and their overall results, sorted by score"""
        
        return self.player_result_handler.ToStringTable()
 
    def GetDateRange(self):
        return self.date_range
        
    def GetDateIndexList(self):
        return self.date_index_list
        
    def GetType(self):
        return self.tournament_type
 
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
        
    def IsCurrent(self):
        return self.is_current
        
    def Conflicts(self, t): 
        d_r = t.GetDateRange()
        test = 0
        for d in d_r:
            if d in self.GetDateRange():
                test = 1
                break
        return test
        
    #Maintenance Functions
    def DailyMaintenance(self, players):
        self.SendInvites(players)
        
    def AddStartDate(self, start_date):
        self.start_date = start_date
        self.UpdateRow("date", start_date)
        
    def AddDateRange(self, date_range):
        self.date_range = date_range
        self.AddStartDate(date_range[0])
        self.UpdateRow("date", str(date_range[0].GetDate()))
    
    def AddPlayer(self, p):
        """adds single player to tournament"""
        
        if len(self.player_list) < self.max_players:
            if not p in self.player_list:
                if self.player_requirements.Test(p):
                    if p.player_tournament_handler.AddNewTournament(self):
                        self.player_list.append(p)
                        self.UpdateNumPlayers(1)
                    return 1
        return 0
        
    def UpdateNumPlayers(self, num):
        self.num_players += num
        self.UpdateRow("players", self.num_players)

    def AddPlayers(self, players):
        """adds a list of players to the tournament"""
        
        for new_player in players:
            self.AddPlayer(new_player)
            
    def SendInvites2(self, players):
        """Takes a list of players and sends invites to certain ones"""
        
        #basic implementation, invites everyone who passes the basic requirements of the tournament
        for p in players:
            if self.player_requirements.Test(p):
                accept = p.EvaluateInvite(self)
                if accept:
                    self.AddPlayer(p)
                
    def SendInvites(self, players):
        """new implementation of SendInvites"""
        
        #could probably just index player list with random numbers, would be faster.
        random.shuffle(players)
        
        if not self.players_invited:
            """initialize players_invited dict if it doesn't already exist"""
            temp_list = []
            for p in players:
                temp_list.append((p.GetPlayerNum(), 1))
            self.players_invited = dict(temp_list)
            
        for p in players:
            """now invite players that haven't been invited yet"""
            if len(self.sent_invites) < self.max_players:
                if self.players_invited[p.GetPlayerNum()]:
                    if self.player_requirements.Test(p):
                        if random.choice([1,0,0,0]):
                            temp_invite = cts.tournament.invitation.invitation(self, p, self.AddPlayer, self.DeclineInvite)
                            p.AddTournamentInvite(temp_invite)
                            self.sent_invites.append(temp_invite)
                            self.players_invited[p.GetPlayerNum()] = 0
            else:
                break
                
        self.sent_invites_st.ReplaceRows(self.sent_invites)         #update string table of sent_invites
    
    def DeclineInvite(self, invitation):
        """called by player when declining an invitation"""
        if invitation in self.sent_invites:
            self.sent_invites.remove(invitation)

    #Play Functions            
    def PlayTournament(self):
        while not self.schedule_handler.IsFinished():
            self.PlayCurrentRound()
    
    def PlayCurrentRound(self):
        """plays the current round, then sends the results to the player result handler.
        
        note: WHY AM I STILL USING PLAYER_RESULT_HANDLER's??? This should be replaced by string
        tables and rows functionality!!!"""
        
        round_played = self.schedule_handler.PlayCurrentRound()
        if round_played:
            temp_results = self.schedule_handler.GetRoundResults()
            self.player_result_handler.AddRoundResults(temp_results)
            return 1
        else:
            return 0
   
    #Player Interface/Menu Functions
    def DisplayResults(self):
        if self.results_st:
            self.results_st.SortBy('score', ascending=0)
            DisplayStringTable(self.results_st, pause=1)
        else:
            print "ah, crap"
       
    #String Functions
    def ViewGeneral(self):
        self.player_st.ReplaceRows(self.player_list)
        DisplayStringTable(self.player_st, pause=1)
        
    def ViewSentInvites(self):
        DisplayStringTable(self.sent_invites_st, pause=1)
            
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