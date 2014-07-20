class result:
    def __init__(self, white_win, draw):
        self.white_win = white_win
        self.draw = draw
        
    def IsWhiteWin(self):
        return self.white_win
        
    def IsBlackWin(self):
        ret = 0
        if not self.white_win:
            if not self.draw:
                ret = 1
        return ret
        
    def WhiteResult(self):
        white_result = 0
        if self.white_win:
            white_result = 1
        elif self.draw:
            white_result = .5
        return white_result
        
    def BlackResult(self):
        black_result = 1
        if self.draw:
            black_result = .5
        elif self.white_win:
            black_result = 0
        return black_result
        
    def IsDraw(self):
        return self.draw
        
    def ToString(self):
        retstr = ""
        if self.white_win:
            retstr = "1 - 0"
        elif self.draw:
            retstr = ".5-.5"
        else:
            retstr = "0 - 1"
            
        return retstr