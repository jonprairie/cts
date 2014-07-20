from cts.options.header import *
import cts.application.stackable as stackable
import calendarhandler
import playerhandler
import tournamenthandler    

class gameinstance(stackable.stackable):
    """Main game level, this is where the game mechanics are implemented"""
    
    def __init__(self):
        self.menu_list = [("back", [], self.MakeExit),
                          ("sim day", [], self.SimDay),
		                  ("play tournament", [], self.dummyPlayTournament),
                          ("official player list", [], self.DisplayTopPlayers)]
    
        stackable.stackable.__init__(self, self.menu_list, "Main Menu")
        
        self.player_handler = playerhandler.playerhandler()
        self.calendar_handler = calendarhandler.calendarhandler()
        self.tournament_handler = tournamenthandler.tournamenthandler()

        self.InitGame()
        
    def InitGame(self):
        self.player_handler.InitPlayers()
        self.tournament_handler.GenInitialTournaments(self.calendar_handler.GetCurrentDate())
        self.PopulateInitialTournaments()
        
        self.DailyMaintenance()
        self.WeeklyMaintenance()
    
    #Maintenance Functions
    def PopulateInitialTournaments(self):
        """Populates the tournaments that are initialized at the start of a new game"""
        
        self.PopulateTournaments()
    
    def PopulateTournaments(self):
        """Sends invites to players from 'Invitational' (non-open) tournaments.
        Then registers players for open tournaments."""
        
        self.tournament_handler.SendInvites(self.player_handler.GetPlayers())
        self.player_handler.RegisterForTournaments(self.tournament_handler.GetNewTournaments())

    def MonthlyMaintenance(self):
        pass
        
    def WeeklyMaintenance(self):
        pass
        
    def DailyMaintenance(self):
        #Tournament Handler Maintenance
        current_date = self.calendar_handler.GetCurrentDate()
        self.tournament_handler.NewTournamentMaintenance(current_date)
        transfers = self.tournament_handler.WaitingTournamentMaintenance(current_date)
        self.tournament_handler.CurrentTournamentMaintenance()
        for t in transfers:
            t_range = t.GetNumRounds()
            self.calendar_handler.AddTournamentToRange(t, t_range)

    #Player Interface/Menu Functions
    def SimDay(self):
        current_date = self.calendar_handler.GetCurrentDate()
        current_tournaments = current_date.GetTournaments()
        
        for t in current_tournaments:
            t.PlayCurrentRound()
            
        self.calendar_handler.IncrementDay()
        self.DailyMaintenance()
        if self.calendar_handler.IsWeek():
            self.WeeklyMaintenance()
            
    def DisplayTopPlayers(self, num_players=50):
        player_list = self.player_handler.GetPlayers()
        player_list.sort(cmp = playerhandler.PlayerCMP)
        player_table = []
        
        for player, num in zip(player_list, range(num_players)):
            temp_row = []
            temp_row.append(str(num+1) + ":")
            temp_row.append(player.GetName())
            temp_row.append(str(player.GetElo()))
            temp_row.append(str(player.GetElo("lelo")))
            player_table.append(temp_row)
        
        DisplayTable(player_table)
 
    def dummyPlayTournament(self):
        for t in self.tournament_handler.GetCurrentTournaments():
            self.PassControl(t)