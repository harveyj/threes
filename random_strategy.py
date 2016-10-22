import random, copy
from consts import *
import threes_strategy
import board

class RandomStrategy(threes_strategy.Strategy):
    def __init__(self, board):
        super(RandomStrategy, self).__init__(board)

    ## DOESN'T WORK YET
    def get_next_move(self):
        if not can_move(self.board.cell_store):
            print "BLOCKED"
            print self.board
            return None
        return random.randint(0,3)


def can_move(cells):
    b = board.Board()
    l_copy = b.transform(copy.deepcopy(cells), LEFT)
    r_copy = b.transform(copy.deepcopy(cells), RIGHT)
    u_copy = b.transform(copy.deepcopy(cells), UP)
    d_copy = b.transform(copy.deepcopy(cells), DOWN)
    return b == l_copy == r_copy == u_copy == d_copy
