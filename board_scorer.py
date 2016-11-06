from consts import *
from board_generator import *

class BoardScorer(object):
    def __init__(self, brd):
        self.board = brd

    def combined(self):
        return (
            self.free_moves() +
            self.empties() + 
            self.inversions() + 
            self.weighted() + 
            self.num_one_or_two() + 
            self.max() +
            self.max_down_right()
            )

    def weighted(self):
        c = self.board.cell_store
        sum = ( c[0][0] * 0 + c[0][1] * 1 + c[0][2] * 3 + c[0][3] * 4 +
                c[1][0] * 0 + c[1][1] * 0 + c[1][2] * 2 + c[1][3] * 4  +
                c[2][0] * 0 + c[2][1] * 0 + c[2][2] * 1 + c[2][3] * 6  +
                c[3][0] * 0 + c[3][1] * 1 + c[3][2] * 1 + c[3][3] * 8
                )
        return sum / 192.0

    def inversions(self):
        cells = self.board.cell_store
        num_inversions = 0
        for r in cells:
            c_last = 0
            for c in r:
                if c < c_last:
                    num_inversions += 1
                c_last = c

        for r in zip(*cells):
            c_last = 0
            for c in r:
                if c < c_last:
                    num_inversions += 1
                c_last = c

        if num_inversions == 0: return 1
        else: return 1.0 / num_inversions

    def free_moves(self):
        ab = BoardGenerator(self.board).all_boards()
        l_brd, r_brd, u_brd, d_brd = (ab[LEFT], ab[RIGHT], ab[UP], ab[DOWN])
        free_moves = 0

        if self.board != l_brd:
            free_moves += 1
        if self.board != u_brd:
            free_moves += 1

        return free_moves / 2.0

    def num_one_or_two(self):
        n = 0
        for r in self.board.cell_store:
            for c in r:
                if c in [1, 2]:
                    n += 1
        return 1 - n / 16.0

    def max_down_right(self):
        if self.board.max_value() == self.board.cell_store[3][3]:
            return 2.0
        return 0

    def empties(self):
        n = 0
        for r in self.board.cell_store:
            for c in r:
                if c == 0:
                    n += 1
        return n / 16.0

    def max(self):
        import math
        return math.log(self.board.max_value())




