import linkedhandler
from cts.options.header import *
import date
import datetime
import calendar

class calendarhandler(linkedhandler.linkedhandler):
    """generates and maintains the calendar for the gameinstance, also acts as a 'clock', sending a 'signal' to
    the tournament and player handler every day, week, and month"""
    
    def __init__(self):
        self.current_date = datetime.date(default_options["start_year"], default_options["start_month"], default_options["start_day"])
        self.current_date_index = 0
        self.date_list = []
        self.InitDateList()
        
        self.player_handler = 0
        self.tournament_handler = 0
   
    def InitDateList(self):
        current_date_ordinal = self.current_date.toordinal()
        for day in range(default_options["game_length"]):
            temp_date = datetime.date.fromordinal(current_date_ordinal + day)
            temp_date = date.date(date = temp_date)
            self.date_list.append(temp_date)
    
    #Get Functions
    def GetCurrentDate(self):
        return self.date_list[self.current_date_index]
        
    def GetDate(self, date_index):
        """returns the date corresponding to the current date's index + date_index"""
        return self.date_list[self.current_date_index + date_index]

    def GetDateRange(self, start_date, index_list):
        """takes a start date and a list of indexes and returns a list of the dates corresponding to the 
        indexes, relative to the start date's index"""

        if start_date in self.date_list:
            ret_list = []
            start_date_index = self.date_list.index(start_date)
            for day in index_list:
                temp_date = self.date_list[start_date_index + day]
                ret_list.append(temp_date)
            return ret_list

    #Test Functions
    def IsWeek(self):
        ret_bool = self.current_date_index % 7
        return not ret_bool
        
    def IsMonth(self):
        ret_bool = self.current_date_index % 30
        return not ret_bool
    
    #Maintenance Functions
    def IncrementDay(self):
        self.current_date_index += 1

        self.federation_handler.DailyMaintenance()
        
        self.tournament_handler.DailyMaintenance()
            
        self.player_handler.DailyMaintenance()

        if self.IsWeek():
            self.federation_handler.WeeklyMaintenance()
            self.tournament_handler.WeeklyMaintenance()
            self.player_handler.WeeklyMaintenance()
        if self.IsMonth():
            self.federation_handler.MonthlyMaintenance()
            self.tournament_handler.MonthlyMaintenance()
            self.player_handler.MonthlyMaintenance()
            