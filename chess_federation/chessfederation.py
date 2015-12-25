import cts.application.row
import cts.application.stringtable
import cts.chess_federation.country
import cts.tournament.tournament
import cts.utils

class chessfederation(cts.application.row.row):
    def __init__(self, country, ch_date=7):
        self.country = country                  #associated country
        self.ch_date = ch_date                  #date on which to hold the federation's championship tournament each year
        self.player_list = []
        self.name=self.GenName()
        self.ch_tournament_list = []            #list of past championships
        self.current_championship = 0           #championship tournament for current year
        self.tournament_list = []
        self.waiting_tournament_list = []
        self.player_st = cts.application.stringtable.stringtable(self.country.Adjective()+" players", self.player_list)
        
        cts.application.row.row.__init__(self, dict(name=self.name, country=self.country.GetName()))
  
    def __str__(self):
        return self.name
        
    def GetName(self):
        return self.name
        
    def GetCountry(self):
        return self.country
        
    def IsChWaiting(self):
        return self.ch_waiting
        
    def PullTournaments(self):
        ret_list = self.waiting_tournament_list[:]
        self.waiting_tournament_list = []
        return ret_list
    
    def GenName(self):
        return self.country.Adjective() + " chess federation"
        
    def AddPlayer(self, player):
        if player not in self.player_list:
            self.player_list.append(player)
            self.player_st.ReplaceRows(self.player_list)
            return 1
        return 0
        
    def AddPlayerList(self, player_list):
        for player in player_list:
            self.AddPlayer(player)
            
    def GenNextChampionship(self):
        """basic version, only creates a championship if there is no current_championship"""
        if not self.current_championship:
            self.current_championship = cts.tournament.tournament.tournament(self.country.Adjective() + " championship", start_date = self.ch_date, open = 0, tournament_type = "round robin", double_rr = 0)
            self.tournament_list.append(self.current_championship)
            self.waiting_tournament_list.append(self.current_championship)
            self.current_championship.AddPlayerRequirement("p.GetCountry().GetName() is '" + self.country.GetName() + "'")  
            
class parentfederation(chessfederation):
    def __init__(self):
        self.children_federations = self.BuildChildrenFederations()
        chessfederation.__init__(self, cts.chess_federation.country.world)
        
    def BuildChildrenFederations(self):
        ret_list = []
        for c in cts.chess_federation.country.country_list:
            temp_fed = chessfederation(c)
            temp_fed.GenNextChampionship()
            ret_list.append(temp_fed)
        return ret_list
        
    def RegisterPlayers(self, player_list):
        c_fed_dict = cts.utils.ExtractToDict(self.children_federations, chessfederation.GetCountry)
        for p in player_list:
            if p.GetCountry() in c_fed_dict.keys():
                if c_fed_dict[p.GetCountry()].AddPlayer(p):
                    p.SetFederation(c_fed_dict[p.GetCountry()])
        
    def PullChildrenTournaments(self):
        ret_list = []
        for c_fed in self.children_federations:
            ret_list.extend(c_fed.PullTournaments())
        return ret_list