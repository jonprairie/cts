class playerresults:
    def __init__(self, tournament, player):
        self.tournament = tournament
        self.player = player
        self.player_games = []
        
    def AddGame(self, game):
        self.player_games.append(game)
        
    def GetPlayer(self):
        return self.player
        
    def GetScore(self):
        score = 0
        for game in self.player_games:
            if not game.IsBye():
                score += game.GetPlayerResult(self.player)
        return score
        
    def GetName(self):
        return self.player.GetName()
        
    def SwitchOnResult(self, result):
        """returns -1 for a loss, 0 for a draw and 1 for a win"""

        temp_result = 2*result
        temp_result -= 1
        return temp_result

    def GetPerformanceRating(self):
        performance_rating = 0
        total_rating = 0
        temp_rating = 0
        for game in self.player_games:
            temp_rating = game.GetOpponent(self.player).GetElo()
            temp_rating += (400 * self.SwitchOnResult(game.GetPlayerResult(self.player)))
            total_rating += temp_rating
        if self.NumGamesPlayed():
            performance_rating = total_rating / self.NumGamesPlayed()
        return performance_rating
        
    def NumGamesPlayed(self):
        num = 0
        for game in self.player_games:
            if not game.IsBye():
                num += 1
        return num
    