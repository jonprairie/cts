#dictionary of default game options
def_elo = 2400
options_dict = dict(
    #player options
    real_player_elo = 1800,
    corresponding_elo = 2650,
        
    #calendar options
    start_year = 2014,
    start_month = 1,
    start_day = 1,
            
    #chess options
    time_control = (45,0,0,45),
            
    #cpu player options
    elo = def_elo,
    elo_dict = dict(elo=def_elo, telo=def_elo, topelo=def_elo, tmgelo=def_elo, tenelo=def_elo, lelo=def_elo),
    player_fame = 50,
            
    #tournament options
    tournament_prestige = 50,
    tournament_rounds = 7,
    tournament_type = "round robin",
    double_rr = 0,
    round_robin_player_range = (4, 10),
    swiss_player_range = (10, 100)
    )