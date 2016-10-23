import copy
import board, threes_strategy
import board_scorer
from consts import *
from getch import *
from board_generator import *

DEBUG=False

class RecurseStrategy(threes_strategy.Strategy):
    def __init__(self, brd, depth=2):
        super(RecurseStrategy, self).__init__(brd)
        self.depth = int(depth)
        self.wait = False

    def get_next_move(self):
        dir = self.get_move_direction(self.board)
        print self.board.max_value()
        if self.wait:
            print self.board
            getch()
        return dir

    def get_move_direction(self, brd):
        ab = BoardGenerator(brd).all_boards()
        l_brd, r_brd, u_brd, d_brd = (ab[LEFT], ab[RIGHT], ab[UP], ab[DOWN])

        l = self.score_recurse(l_brd, self.depth)
        if l_brd == brd:
            l = -1
        r = self.score_recurse(r_brd, self.depth)
        if r_brd == brd:
            r = -1
        u = self.score_recurse(u_brd, self.depth)
        if u_brd == brd:
            u = -1
        d = self.score_recurse(d_brd, self.depth)
        if d_brd == brd:
            d = -1

        if DEBUG:
            print u, d, l, r
        if u == d == r == l == -1:
            return None

        dir = LEFT
        max = l
        if u > max:
            max = u
            dir = UP
        if r > max:
            max = r
            dir = RIGHT
        if d > max:
            max = d
            dir = DOWN
        return dir

    def score_individual(self, brd):
        scorer = board_scorer.BoardScorer(brd)
#        return scorer.weighted()
#        return 1.0 / scorer.count_inversions()
        return self.score_combined(brd)

    def score_combined(self, brd):
        scorer = board_scorer.BoardScorer(brd)
        return (
            scorer.free_moves() +
            scorer.empties() + 
#           scorer.inversions() + 
            scorer.max()
            )

    def score_recurse(self, brd, n):
        ab = BoardGenerator(brd).all_boards()
        l_brd, r_brd, u_brd, d_brd = (ab[LEFT], ab[RIGHT], ab[UP], ab[DOWN])
        if n == 0:
            l = self.score_individual(l_brd)
            r = self.score_individual(r_brd) + 1
            u = self.score_individual(u_brd)
            d = self.score_individual(d_brd) + 1
        else:
            l = self.score_recurse(l_brd, n - 1)
            r = self.score_recurse(r_brd, n - 1)
            u = self.score_recurse(u_brd, n - 1)
            d = self.score_recurse(d_brd, n - 1)
        return max([l, r, u, d])

