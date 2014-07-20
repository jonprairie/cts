from cts.options.header import *
import cts.chess_game.chessgame as chessgame

class round:
    """single round of a tournament"""

    def __init__(self, round_number, round_schedule = [], time_control = default_options["time_control"]):
        self.round_number = round_number
        self.round_schedule = []
        self.time_control = time_control
        self.is_finished = 0
        
        for game in round_schedule:
            self.AddGame(game[0], game[1])
            
    def AddGame(self, white, black):
        temp_game = chessgame.chessgame(white, black, self.time_control)
        self.round_schedule.append(temp_game)
            
    def PlayRound(self):
        if not self.is_finished:
            for game in self.round_schedule:
                game.Play()
        self.is_finished = 1
        
    def IsFinished(self):
        return self.is_finished
            
    def SetRoundNumber(self, round_number):
        self.round_number = round_number
        
    def GetGames(self):
        return self.round_schedule
        
    def ToString(self):
        roundstring = "round " + str(self.round_number) + ": \n"
        for game in self.round_schedule:
            temp_string = " " + game.ToString(show_elo=1) + "\n"
            roundstring += temp_string
        return roundstring