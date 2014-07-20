class date:
    def __init__(self, date = 0, tournaments = []):
        self.date = date
        self.tournaments = tournaments

    def SetDate(self, date):
        self.date = date
        
    def AddTournament(self, tournament):
        if not self.tournaments.count(tournament):
            self.tournaments.append(tournament)
        
    def GetTournaments(self):
        return self.tournaments
        
    def GetDate(self):
        return self.date
    