from cts.options.header import *
from clock import *

class chessgame:
    """chess game"""

    def __init__(self, player_w, player_b, time_control = default_options["time_control"]):
        
        self.player_w = player_w
        self.player_b = player_b
        self.time_control = time_control
        self.clock = clock(time_control)
        self.move_list = []
        self.result = 0
        self.is_finished = 0
        self.bye = 0
        self.player_on_bye = 0
        
        if not self.player_b:
            self.bye = 1
            self.player_on_bye = self.player_w
        if not self.player_w:
            self.bye = 1
            self.player_on_bye = self.player_b
            
    #Get Functions        
    def GetPlayerResult(self, player):
        player_result = 0
        if self.IsFinished():
            if not self.IsBye():
                if player is self.player_w:
                    player_result = self.result.WhiteResult()
                elif player is self.player_b:
                    player_result = self.result.BlackResult()
        return player_result        
         
    def GetOpponent(self, player):
        if not self.IsBye():
            if self.player_w is player:
                return self.player_b
            elif self.player_b is player:
                return self.player_w
            else:
                return 0
        else:
            return "bye"   
            
    def GetResult(self):
        return self.result
        
    def GetWhitePlayer(self):
        return self.player_w
        
    def GetBlackPlayer(self):
        return self.player_b        
    
    #Test Functions
    def IsFinished(self):
        return self.is_finished

    def IsBye(self):
        return self.bye
    
    #Play/Sim Functions
    def Play(self):
        if not self.is_finished:
            if not self.IsBye():
                self.result = stats_model.SimulateResult(self.player_w.GetElo("telo"), self.player_b.GetElo("telo"))
                w_adjustment, b_adjustment = stats_model.RatingAdjustment(self.player_w.GetElo("lelo"), self.player_b.GetElo("lelo"), self.result)
                self.player_w.UpdateElo(w_adjustment)
                self.player_b.UpdateElo(b_adjustment)
            self.is_finished = 1

    #String Functions
    def ToString(self, show_elo=0, show_title=0):
        """returns a string: 'white vs black'"""
        if not self.IsBye():
            retstr = ""
            wpstr = ""
            bpstr = ""
            
            if show_elo:
                wpstr += str(self.player_w.GetElo("elo")) + " "
                bpstr += str(self.player_b.GetElo("elo")) + " "
                
            wpstr += self.player_w.GetName()
            bpstr += self.player_b.GetName()
            
            retstr += wpstr
            retstr += " vs "
            retstr += bpstr
            
            if self.IsFinished():
                retstr += " "
                retstr += self.result.ToString()
            
            return retstr
            
        else:
            return "Bye: " + self.player_on_bye.GetName()
            