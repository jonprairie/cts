class linkedhandler:
    def __init__(self):
        pass
        
    def LinkHandlers(self, player_handler = 0, calendar_handler = 0, tournament_handler = 0, federation_handler = 0):
        if player_handler:
            self.player_handler = player_handler
        if calendar_handler:
            self.calendar_handler = calendar_handler
        if tournament_handler:
            self.tournament_handler = tournament_handler
        if federation_handler:
            self.federation_handler = federation_handler