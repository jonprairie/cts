class ranking:
    def __init__(self, ranking, player_list):
        self.ranking = ranking
        self.player_list = player_list
        self.tie = 0
        self.UpdateTie()
        
    def UpdateTie(self):
        pl_len = len(self.player_list)
        if pl_len is not 1:
            self.tie = self.ranking + pl_len -1
            
    def GetScore(self):
        return self.player_list[0].GetScore()
            
    def AddPlayer(self, player):
        self.player_list.append(player)
        self.UpdateTie()
        
    def GetRanking(self):
        return self.ranking, tie
        
    def MakeRanking(self, ranking, tie):
        self.ranking = ranking
        self.tie = tie
        
    def IsEqual(self, cts_ranking):
        ranking, tie = cts_ranking.GetRanking()
        if ranking is self.ranking:
            if tie is self.tie:
                return 1
        return 0
        
    def IsGreater(self, ranking):
        pass
        
    def ToStringTable(self, show_performance_rating = 1, show_elo = 1):
        ret_table = []
        header_row = []
        temp_row = []
        
        if not self.tie:
            temp_row.append(str(self.ranking))
        else:
            temp_string = str(self.ranking) + "-" + str(self.tie)
            temp_row.append(temp_string)
        
        first = 1
        for player in self.player_list:
            if first:
                temp_row.extend(self.FinishRow(player, show_performance_rating, show_elo))
                first = 0
            else:
                temp_row = []
                temp_row.append("")
                temp_row.extend(self.FinishRow(player, show_performance_rating, show_elo))
            ret_table.append(temp_row)
        return ret_table
                
                
    def FinishRow(self, player, show_performance_rating = 1, show_elo = 1):
        temp_row = []
        temp_row.append(player.GetName())
        temp_string = str(player.GetScore()) + "/" + str(player.NumGamesPlayed())
        temp_row.append(temp_string)        
        if show_elo:
            temp_string = str(player.GetPlayer().GetElo())
            temp_row.append(temp_string)
        if show_performance_rating:
            temp_string = str(player.GetPerformanceRating())
            temp_row.append(temp_string)
        return temp_row
            
    def ToString(self):
        retstr = ""
        if not self.tie:
            retstr += str(self.ranking)
        else:
            retstr += str(self.ranking)
            retstr += "-"
            retstr += str(self.tie)
        retstr += " "
        strlen = len(retstr)
        notfirst = 0
        notlast = 1
        for player, p_index in zip(self.player_list, range(len(self.player_list))):
            if notfirst:
                for buff in range(strlen):
                    retstr += " "
            retstr += player.GetPlayer().GetName()
            retstr += " "
            retstr += str(self.GetScore())
            if p_index is (len(self.player_list)-1):
                notlast = 0
            if notlast:    
                retstr += "\n"
            if not notfirst:
                notfirst = 1
        return retstr
        