class clock:
    def __init__(self, (first, second, third, inc)):
        
        self.first = first            #control for first 40 moves, in minutes
        self.second = second        #control for second 40 moves
        self.third = third            #control for third 40 moves
        self.inc = inc                #increment in seconds, applies to all 3 controls
        
        self.wtime = self.first
        self.btime = self.first
        self.wmoves = 0
        self.bmoves = 0
