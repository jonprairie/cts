from cts.options.header import *
import gamestack
import mainmenu

class main:
    """Main application level, uses a Stack model to handle gamestate"""
    
    def __init__(self):
        self.main_menu = mainmenu.mainmenu()
        game_stack.Append(self.main_menu)
    
    def MainLoop(self):
        while not game_stack.IsEmpty():
            game_stack.PeekLoop()
            if game_stack.PeekIsExit():
                temp = game_stack.Pop()
                temp.ResetExit()

if __name__ == "__main__":
    cts = main()
    cts.MainLoop()