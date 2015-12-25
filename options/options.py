#dictionary of default game options
def_elo = 2400
options_dict = dict(
    #human player options
    real_player_elo = 1800,
    corresponding_elo = 2650,
            
    #cpu player options
    num_initial_cpu_players = 500,
    elo = def_elo,
    player_fame = 50,

    #player generation options
    play_strength_mu = 2500,
    play_strength_sigma = 100,
    
    #calendar options
    game_length = 730, #in days, 730 = 2 years
    start_year = 2015,
    start_month = 1,
    start_day = 18,
            
    #chess game options
    time_control = (45,0,0,45),
            
    #tournament options
    tournament_prestige = 50,
    tournament_prestige_decay_factor = 1,
    tournament_rounds = 7,
    tournament_rest_days = 2,
    tournament_type = "round robin",
    double_rr = 0,
    round_robin_player_range = (4, 10),
    swiss_player_range = (10, 100)
    )