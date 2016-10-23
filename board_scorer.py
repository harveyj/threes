from consts import *

class BoardScorer(object):
    def __init__(self, board):
        self.board = board

    def weighted(self):
        c = self.board.cell_store
        return (c[3][3] * 128 + c[2][3] * 64 + c[1][3] * 32 + c[0][3] * 24 +
                c[3][2] * 64  + c[2][2] * 16 + c[1][2] * 16 + c[0][2] * 8  +
                c[3][1] * 32  + c[2][1] * 16 + c[1][1] * 8  + c[0][1] * 4  +
                c[3][0] * 24  + c[2][0] * 8  + c[1][0] * 4  + c[0][0] * 2  +
                )

    # Wow. I couldn't have done something this horrible if I tried.
    def count_inversions(self):
        cells = self.board.cell_store
        num_inversions = 0
        for r in cells:
            c_last = 0
            for c in r:
                if c != 0:
                    if c < c_last: num_inversions += 1
                    if c != 0: c_last = c

        for r in zip(*cells):
            c_last = 0
            for c in r:
                if c < c_last: num_inversions += 1
                if c != 0: c_last = c

        if num_inversions == 0: return 1
        else: return 1/num_inversions


