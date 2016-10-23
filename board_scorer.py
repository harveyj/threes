from consts import *
from board_generator import *

class BoardScorer(object):
    def __init__(self, board):
        self.board = board

    def weighted(self):
        c = self.board.cell_store
        return (c[3][3] * 128 + c[2][3] * 64 + c[1][3] * 32 + c[0][3] * 24 +
                c[3][2] * 64  + c[2][2] * 16 + c[1][2] * 16 + c[0][2] * 8  +
                c[3][1] * 32  + c[2][1] * 16 + c[1][1] * 8  + c[0][1] * 4  +
                c[3][0] * 24  + c[2][0] * 8  + c[1][0] * 4  + c[0][0] * 2
                )

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




