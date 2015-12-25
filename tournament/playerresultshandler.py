import playerresults
import ranking

class playerresultshandler:
    """player results handler, generates and maintains the list of player results for a tournament"""
    
    def __init__(self, tournament, player_list):
        self.tournament = tournament
        self.player_handler_list = []
        self.player_rankings = []
        
        self.InitPHList(player_list)
        
    def GetList(self):
        return self.player_handler_list
        
    def InitPHList(self, player_list):
        for player in player_list:
            temp = playerresults.playerresults(self.tournament, player)
            self.player_handler_list.append(temp)
        
    def AddRoundResults(self, round):
        for game in round:
            for player in self.player_handler_list:
                if game.GetWhitePlayer() is player.GetPlayer():
                    player.AddGame(game)
                elif game.GetBlackPlayer() is player.GetPlayer():
                    player.AddGame(game)
                    
    def SortPlayers(self, break_ties = 0):
        self.player_rankings = []
        ranking_list = []
        for player_1 in self.player_handler_list:
                inserted_flag = 0
                for player_2, index in zip(ranking_list, range(len(ranking_list))):
                    if player_1.GetScore() > player_2.GetScore():
                        ranking_list.insert(index, player_1)
                        inserted_flag = 1
                        break
                if not inserted_flag:
                    ranking_list.append(player_1)
        
        for player, index in zip(ranking_list, range(len(ranking_list))):
            inserted_flag = 0
            for rank in self.player_rankings:
                if abs(rank.GetScore() - player.GetScore()) < .2:
                    rank.AddPlayer(player)
                    inserted_flag = 1
                    break
            if not inserted_flag:
                temp = ranking.ranking(index+1, [player])
                self.player_rankings.append(temp)
                        
    def Score(self, player):
        return player.GetScore()
        
    def ToString(self):
        retstr = ""
        for rank in self.player_rankings:
            retstr += rank.ToString()
            retstr += "\n"
        return retstr
        
    def ToStringTable(self, show_performance_rating = 1, show_elo = 1):
        ret_table = []
        header_row = []
        header_row.append("RANK")
        header_row.append("NAME")
        header_row.append("SCORE")
        if show_elo:
            header_row.append("ELO")
        if show_performance_rating:
            header_row.append("P RATING")
        ret_table.append(header_row)
        self.SortPlayers()
        for rank in self.player_rankings:
            ret_table.extend(rank.ToStringTable(show_performance_rating, show_elo))
        return ret_table