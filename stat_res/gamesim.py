from random import uniform
import cts.tournament.result as result

class gamesim:
    def __init__(self):
        self.k_factor = 8
        
    def ExpectedValue(self, r_a, r_b):
        """expected value for players a and b.
        r_a is the rating of player a"""
        
        diff = float(r_a - r_b)
        
        e_a = 1/(1+10**(-diff/400))
        e_b = 1-e_a
        
        if e_a < .02:
            e_a = .02
            e_b = .98
            
        if e_b < .02:
            e_b = .02
            e_a = .98
            
        return e_a, e_b
        
    def RatingAdjustment(self, r_a, r_b, res):
        """result is instance of result. r_a is assumed to be the rating
        of the white player, r_b the black player"""
        
        e_a, e_b = self.ExpectedValue(r_a, r_b)
        
        ra_a = self.k_factor*(res.WhiteResult() - e_a)
        ra_b = -ra_a
        
        return ra_a, ra_b

    def DrawProbability(self, r_a, r_b):
        """provides a simple model for the probability of a draw between two players of ratings r_a and r_b"""

        draw_probability_ceiling = .5
        draw_probability_floor = .01
        draw_probability = draw_probability_ceiling -.001 * abs(r_a-r_b)
        
        if draw_probability < draw_probability_floor:
            draw_probability = draw_probability_floor
        if draw_probability > draw_probability_ceiling:
            draw_probability = draw_probability_ceiling
        
        return draw_probability
    
    def IsDraw(self, e_a, draw_probability):
        
        random_float = uniform(0, e_a)
        is_draw = .5 * draw_probability
        
        if random_float <= is_draw:
            return 1
        else:
            return 0
        
    def SimulateResult(self, r_a, r_b):
        """takes r_a and r_b, the ratings of the white and black player, 
        and simulates the result of a game played between them, returning the result."""
        
        draw_probability = self.DrawProbability(r_a, r_b)
        e_a, e_b = self.ExpectedValue(r_a, r_b)
        white_win = 0
        is_draw = 0
        res = 0
        
        random_float = uniform(0,1)
        
        if random_float <= e_a:
            value = 1
            is_draw = self.IsDraw(e_a, draw_probability)
        else:
            value = 0                                            
            is_draw = self.IsDraw(e_b, draw_probability)
        
        if not is_draw:
            if value:
                white_win = 1
        
        res = result.result(white_win, is_draw)
        return res
        