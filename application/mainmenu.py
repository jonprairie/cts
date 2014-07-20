from cts.options.header import *
import stackable
import cts.game_instance.gameinstance as gameinstance

class mainmenu(stackable.stackable):
    def __init__(self):
        self.menu_list = [("exit", [], self.MakeExit),
		                  ("new game", [], self.NewGame),
                          ("load game", [], self.LoadGame)]
                          
        stackable.stackable.__init__(self, self.menu_list, "Chess Tournament Sim")
        self.current_game = []
        
    def NewGame(self):
        self.current_game = gameinstance.gameinstance()
        self.PassControl(self.current_game)
        
    def LoadGame(self):
        pass 