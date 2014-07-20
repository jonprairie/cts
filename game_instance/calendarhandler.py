from cts.options.header import *
import date
import datetime
import calendar

DEF_GAME_LENGTH = 730       #two years

class calendarhandler:
    def __init__(self):
        self.current_date = datetime.date(default_options["start_year"], default_options["start_month"], default_options["start_day"])
        self.current_date_index = 0
        self.date_list = []
        self.InitDateList()
        
    def InitDateList(self):
        current_date_ordinal = self.current_date.toordinal()
        for day in range(DEF_GAME_LENGTH):
            temp_date = datetime.date.fromordinal(current_date_ordinal + day)
            temp_date = date.date(date = temp_date)
            self.date_list.append(temp_date)
 
    def GetCurrentDate(self):
        return self.date_list[self.current_date_index]

    def IsWeek(self):
        ret_bool = self.current_date_index % 7
        return not ret_bool
    
    def IncrementDay(self):
        self.current_date_index += 1
        
    def AddTournamentToRange(self, tournament, t_range):
        day_index = self.date_list.index(tournament.GetStartDate())
        for day in range(t_range):
            date = self.date_list[day_index + day]
            self.AddTournamentToDate(tournament, date)
        
    def AddTournamentToDate(self, tournament, date):
        date.AddTournament(tournament)