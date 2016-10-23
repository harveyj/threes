import copy
import board, threes_strategy
from consts import *
from getch import *

class RecurseStrategy(threes_strategy.Strategy):
    def __init__(self, board, depth=2):
        super(RecurseStrategy, self).__init__(board)
        self.depth = int(depth)
        self.wait = False

    def get_next_move(self):
        dir = self.get_move_direction(self.board)
        if self.wait:
            print self.board
            getch()
        return dir

    def get_move_direction(self, b):
        ab = all_boards(b.cell_store)
        l_copy, r_copy, u_copy, d_copy = (ab[LEFT], ab[RIGHT], ab[UP], ab[DOWN])

        l = self.score_recurse(l_copy, self.depth)
        if l_copy == b.cell_store:
            l = -1
        r = self.score_recurse(r_copy, self.depth)
        if r_copy == b.cell_store:
            r = -1
        u = self.score_recurse(u_copy, self.depth)
        if u_copy == b.cell_store:
            u = -1
        d = self.score_recurse(d_copy, self.depth)
        if d_copy == b.cell_store:
            d = -1

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

    def score_individual(self, cells):
        b = Board()
        b.cell_score = cells
        scorer = BoardScorer(cells)
        return scorer.weighted()

    def score_combined(self, cells):
        return (self.score_free_moves(cells) +
                self.score_empties(cells) +
                self.score_max(cells))

    def score_max(self, cells):
        import math
        return math.log(self.max_value(cells))

    def max_value(self, cells):
        max = 0
        for r in cells:
            for c in r:
                if c > max:
                    max = c
        return max

    def score_empties(self, cells):
        n = 0
        for r in cells:
            for c in r:
                if c == 0:
                    n += 1
        return n / 16.0

    def score_free_moves(self, cells):
        ab = all_boards(b.cell_store)
        l_copy, r_copy, u_copy, d_copy = (ab[LEFT], ab[RIGHT], ab[UP], ab[DOWN])
        free_moves = 0
        if cells != l_copy:
            free_moves += 1
        if cells != r_copy:
            free_moves += 1
        if cells != u_copy:
            free_moves += 1
        if cells != d_copy:
            free_moves += 1
        return free_moves / 4.0

    def score_recurse(self, cells, n):
        ab = all_boards(b.cell_store)
        l_copy, r_copy, u_copy, d_copy = (ab[LEFT], ab[RIGHT], ab[UP], ab[DOWN])
        if n == 0:
            l = self.score_individual(l_copy)
            r = self.score_individual(r_copy) + 1
            u = self.score_individual(u_copy)
            d = self.score_individual(d_copy) + 1
        else:
            l = self.score_recurse(l_copy, n - 1)
            r = self.score_recurse(r_copy, n - 1)
            u = self.score_recurse(u_copy, n - 1)
            d = self.score_recurse(d_copy, n - 1)
        return max([l, r, u, d])

