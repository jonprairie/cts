import cts.application.gamestack as gamestack
import options
import cts.stat_res.gamesim as gamesim
import cts.display.display as display

game_stack = gamestack.gamestack()

default_options = options.options_dict

stats_model = gamesim.gamesim()

Display = display.Display
DisplayTable = display.DisplayTable