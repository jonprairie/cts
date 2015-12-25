import cts.application.row

class date(cts.application.row.row):
    def __init__(self, date = 0, tournament_list = []):
        self.__str__ = ""
        self.date = date
        self.tournament_list = tournament_list
        #cts.application.row.row(self, str(self.date))
        
    def __str__(self):
        return self.__str__

    def SetDate(self, date):
        self.__str__ = date.isoformat()
        self.date = date
        
    def AddTournament(self, t):
        if not self.tournament_list.count(t):
            self.tournament_list.append(t)
            
    def RemoveTournament(self, t):
        if t in self.tournament_list:
            self.tournament_list.remove(t)
        
    def GetTournaments(self):
        return self.tournament_list
        
    def GetDate(self):
        return self.date
    