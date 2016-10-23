import copy
import board, threes_strategy
import board_scorer
from consts import *
from getch import *
from board_generator import *

DEBUG=False

class DownRightStrategy(threes_strategy.Strategy):
    def __init__(self, brd, depth=2):
        super(DownRightStrategy, self).__init__(brd)
        self.wait = False

    def get_next_move(self):
        dir = self.get_move_direction(self.board)
        if self.wait:
            print self.board
            getch()
        return dir

    def get_move_direction(self, brd):
        ab = BoardGenerator(brd).all_boards()
        l_brd, r_brd, u_brd, d_brd = (ab[LEFT], ab[RIGHT], ab[UP], ab[DOWN])

        if d_brd != brd:
            return DOWN
        elif r_brd != brd:
            return RIGHT
        elif u_brd != brd:
            return UP
        elif l_brd != brd:
            return LEFT
        
        return None

