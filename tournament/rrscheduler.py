from cts.options.header import *
import round
from random import shuffle

class rrscheduler:
    """generates round robin rounds for a tournament schedule"""
    
    def __init__(self, double_rr = default_options["double_rr"], time_control = default_options["time_control"]):
        
        self.double_rr = double_rr
        self.player_list = []
        self.rounds = 0
        self.schedule = []
        self.time_control = time_control
        self.odd = 0
        
    def GetNumRounds(self):
        return self.rounds
        
    def GenSchedule(self, player_list):
        """generates a round robin schedule for a tournament"""
        
        self.player_list = player_list    
        self.round_size = len(self.player_list)    #number of players in each round
        self.rounds = 0
        
        if self.round_size % 2:                    #check if odd number of players
            self.odd = 1
        
        if self.odd:
            self.rounds = self.round_size        #sets number of rounds in tournament for odd number of players
        else:
            self.rounds = self.round_size-1     #even number of players
        
        temp_schedule = self.BuildSchedule()    #builds the schedule
        
        if self.double_rr:
            temp_schedule.extend(self.BuildSchedule(reverse = 1))    #doubles the size of the tournament if double round robin
            self.rounds *= 2
            
        shuffle(temp_schedule)                    #randomly shuffles the rounds around in the schedule
        
        self.schedule = temp_schedule
        
        self.AssignRoundNumbers()                #reassigns round numbers based on round position after shuffle
        
        return self.schedule
        
    def AssignRoundNumbers(self):
        for round,index in zip(self.schedule,range(len(self.schedule))):
            round.SetRoundNumber(index+1)
        
    def BuildSchedule(self, reverse=0):
        temp_round = []
        temp_schedule = []
    
        for r in range(self.rounds):
            temp_round_schedule = self.GenRound(reverse)
            temp_round = round.round(r, round_schedule = temp_round_schedule, time_control = self.time_control)
            
            temp_schedule.append(temp_round)
            
            self.CyclePlayers()
            
        return temp_schedule
        
    def GenRound(self, reverse=0):
        round = 0

        if(self.odd):
            round = self.GenRoundOdd(reverse)
        else:
            round = self.GenRoundEven(reverse)
            
        return round
        
    def CyclePlayers(self):
        temp = self.player_list.pop()
        self.player_list.insert(0, temp)
        
    def GenRoundEven(self, reverse=0):
        game_list = []
        len_players = len(self.player_list)
        half = len_players/2
        half_index = half - 1 
        
        first = self.player_list[:half]
        last = self.player_list[half:]
        
        for player_index in range(half):
            if not reverse:
                temp_game = (first[player_index], last[half_index - player_index])
            else:
                temp_game = (last[half_index - player_index], first[player_index])
            
            game_list.append(temp_game)
        
        return game_list
            
    def GenRoundOdd(self, reverse=0):
        game_list = []
        
        bye_player = self.player_list.pop()
        bye_game = (bye_player, 0)
        game_list.append(bye_game)
        
        game_list.extend(self.GenRoundEven(reverse))
        
        self.player_list.append(bye_player)
        
        return game_list
        