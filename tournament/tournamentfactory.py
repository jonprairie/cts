class tournamentfactory:
    """generates and tracks a periodic (generally yearly) tournament"""

    def __init__(self, name, start_date, tourn_constructor):
        self.name = name
        self.start_date = start_date
        self.tourn_constructor = tourn_constructor
        
        self.past_tourn_list = []
        
    def GenTournament(self):
        curr_tourn = self.tourn_constructor()
        self.past_tourn_list.append(curr_tourn)
        return curr_tourn