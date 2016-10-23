import copy
import board, threes_strategy
import board_scorer
from consts import *
from getch import *
from board_generator import *

DEBUG=False

class LastMoveStrategy(threes_strategy.Strategy):
    def __init__(self, brd, depth=2):
        super(LastMoveStrategy, self).__init__(brd)
        self.wait = False
        self.last_move = LEFT
        self.scorer = board_scorer.BoardScorer(brd)

    def get_next_move(self):
        dir = self.get_move_direction(self.board)
        if self.wait:
            print self.board
            print self.scorer.weighted()
            getch()
        self.last_move = dir
        return dir

    def get_move_direction(self, brd):
        ab = BoardGenerator(brd).all_boards()
        l_brd, r_brd, u_brd, d_brd = (ab[LEFT], ab[RIGHT], ab[UP], ab[DOWN])

        if ab[self.last_move] != brd and self.last_move in [DOWN, RIGHT]:
            return self.last_move
        elif d_brd != brd:
            return DOWN
        elif r_brd != brd:
            return RIGHT
        elif u_brd != brd:
            return UP
        elif l_brd != brd:
            return LEFT
        
        return None

