from random import uniform
import cts.tournament.result as result

DEF_MU = 2500
DEF_SIGMA = 100

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
        
        r_ceiling = 2750
        r_floor = 1400
        draw_percentage_ceiling = .65
        draw_percentage_floor = .2
        draw_percentage_floor_x = 300.0
        draw_probability_floor = .02
        ddp_drm = (draw_percentage_ceiling - draw_percentage_floor)/(r_ceiling - r_floor)
        di_i = r_ceiling - r_ceiling * ddp_drm
        r_mean = (float(r_a)+float(r_b))/2
        r_diff = abs(float(r_a-r_b))
        
        if r_mean > r_ceiling:
            draw_intercept = draw_percentage_ceiling
        elif r_mean < r_floor:
            draw_intercept = draw_percentage_floor
        else:
            draw_intercept = r_mean * ddp_drm - di_i
        
        d_y = draw_percentage_floor - draw_intercept
        d_x = draw_percentage_floor_x
        dy_dx = d_y / d_x
        
        draw_probability = r_diff * dy_dx + draw_intercept
        
        if draw_probability < draw_probability_floor:
            draw_probability = draw_probability_floor
        
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
        