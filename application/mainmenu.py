from cts.options.header import *
import cts.application.node
import stackable
import cts.game_instance.gameinstance as gameinstance

class mainmenu(stackable.stackable):
    def __init__(self):
        self.menu_list = self.BuildMenu()
                          
        stackable.stackable.__init__(self, self.menu_list, "Chess Tournament Sim")
        self.current_game = []
        
    def BuildMenu(self):
        en1 = cts.application.node.exteriornode("exit", self.MakeExit)
        en2 = cts.application.node.exteriornode("new game", self.NewGame)
        en3 = cts.application.node.exteriornode("load game", self.LoadGame)
        return [en1, en2, en3]
        
    def NewGame(self):
        self.current_game = gameinstance.gameinstance()
        self.PassControl(self.current_game)
        
    def LoadGame(self):
        pass