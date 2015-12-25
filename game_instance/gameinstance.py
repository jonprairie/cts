from cts.options.header import *
import cts.application.stackable
import cts.application.stringtable
import cts.application.node
import calendarhandler
import playerhandler
import tournamenthandler
import federationhandler

class gameinstance(cts.application.stackable.stackable):
    """Main game level, this is where the game mechanics are implemented"""
    
    def __init__(self):
     
        #Init Handlers
        self.player_handler = playerhandler.playerhandler()
        self.calendar_handler = calendarhandler.calendarhandler()
        self.tournament_handler = tournamenthandler.tournamenthandler()
        self.federation_handler = federationhandler.federationhandler()
        
        #Link Handlers Together
        self.player_handler.LinkHandlers(calendar_handler = self.calendar_handler, tournament_handler = self.tournament_handler, federation_handler = self.federation_handler)
        self.calendar_handler.LinkHandlers(player_handler = self.player_handler, tournament_handler = self.tournament_handler, federation_handler = self.federation_handler)
        self.tournament_handler.LinkHandlers(player_handler = self.player_handler, calendar_handler = self.calendar_handler, federation_handler = self.federation_handler)
        self.federation_handler.LinkHandlers(player_handler = self.player_handler, calendar_handler = self.calendar_handler, tournament_handler = self.tournament_handler)
        
        #Init Game Instance
        self.player_handler.InitPlayers()
        self.federation_handler.RegisterPlayers()
        self.tournament_handler.GenInitialTournaments(self.calendar_handler.GetCurrentDate())
        
        self.header = self.calendar_handler.GetCurrentDate().GetDate()
        
        self.menu_list = self.BuildMenu()
    
        cts.application.stackable.stackable.__init__(self, self.menu_list, "Main Menu")
           

    #Player Interface/Menu Functions
    def BuildMenu(self):
        ev1 = cts.application.node.exteriornode("back", self.MakeExit)
        ev2 = cts.application.node.exteriornode("sim day", self.SimDay)
        ev3 = cts.application.node.exteriornode("play tournament", self.dummyPlayTournament)
        ev4 = cts.application.node.exteriornode("official player list", self.DisplayTopPlayers)
        in1 = cts.application.node.interiornode("future tournaments", self.tournament_handler.GetWaitingTournaments(), dynamic=1, children_func=self.tournament_handler.GetWaitingTournaments)
        in2 = cts.application.node.interiornode("current tournaments", self.tournament_handler.GetCurrentTournaments(), dynamic=1, children_func=self.tournament_handler.GetCurrentTournaments)
        in3 = cts.application.node.interiornode("tournaments", [in1, in2])
        ev5 = cts.application.node.exteriornode("display tournaments", self.DisplayTournaments)
        return [ev1,ev2,ev3,ev4,ev5,in3]
        
    def SimDay(self):
        """Simulates current day"""
        
        current_date = self.calendar_handler.GetCurrentDate()
        current_tournaments = current_date.GetTournaments()
        
        for t in current_tournaments:
            t.PlayCurrentRound()
            
        self.calendar_handler.IncrementDay()
        self.header = self.calendar_handler.GetCurrentDate().GetDate()
    
    def DisplayTopPlayers(self, num_players=50):
        """DEPRECATED"""
        player_list = self.player_handler.GetPlayers()
        player_list.sort(cmp = playerhandler.PlayerCMP)

        player_table = []
        player_table.append(["RANK", "NAME", "ELO", "LIVE ELO"])
        for p, num in zip(player_list, range(num_players)):
            temp_row = []
            temp_row.append(str(num+1) + ":")
            temp_row.append(p.GetName())
            temp_row.append(str(p.GetElo()))
            temp_row.append(str(p.GetLiveElo()))
            player_table.append(temp_row)
        
        DisplayTable(player_table,pause=1)
        
    def DisplayTournaments(self):
        current_tournament_list = self.tournament_handler.GetCurrentTournaments()
        current_tournament_st = cts.application.stringtable.stringtable("current tournaments", current_tournament_list)
        
        future_tournament_list = self.tournament_handler.GetWaitingTournaments()
        future_tournament_st = cts.application.stringtable.stringtable("future tournaments", future_tournament_list)

        new_tournament_list = self.tournament_handler.GetNewTournaments()
        new_tournament_st = cts.application.stringtable.stringtable("new tournaments", new_tournament_list)        
        
        DisplayStringTable(current_tournament_st)
        DisplayStringTable(future_tournament_st, pre_clear = 0)
        DisplayStringTable(new_tournament_st, pre_clear=0, pause=1)
               
    def dummyPlayTournament(self):
        for t in self.tournament_handler.GetCurrentTournaments():
            self.PassControl(t)