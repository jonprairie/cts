import random

country_adjective_list = ["American", "German", "Russian", "British", "French", "Armenian", "Ukrainian"]
tournament_suffix_list = ["Open", "Invitational", "Closed"]

def GenRandTournamentName():
    first = random.choice(country_adjective_list)
    second = random.choice(tournament_suffix_list)
    ret_str = first + " " + second
    return ret_str