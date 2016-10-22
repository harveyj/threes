import copy
import board, threes_strategy
from consts import *


class RecurseStrategy(threes_strategy.Strategy):
    def __init__(self, board):
        super(RecurseStrategy, self).__init__(board)

    def get_next_move(self):
        return get_move_direction(self.board)


def get_move_direction(b):
    l_copy, r_copy, u_copy, d_copy = all_boards(b.cell_store)

    l = score(l_copy)
    if l_copy == b.cell_store:
        l = -1
    r = score(r_copy)
    if r_copy == b.cell_store:
        r = -1
    u = score(u_copy)
    if u_copy == b.cell_store:
        u = -1
    d = score(d_copy)
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
#    return direction_override(l, r, u, d)
#    print l, r, u, d
    return dir

# LRUD
def all_boards(cells):
    b = board.Board()
    l_copy = b.transform(copy.deepcopy(cells), LEFT)
    r_copy = b.transform(copy.deepcopy(cells), RIGHT)
    u_copy = b.transform(copy.deepcopy(cells), UP)
    d_copy = b.transform(copy.deepcopy(cells), DOWN)
    return (l_copy, r_copy, u_copy, d_copy)

def direction_override(l, r, u, d):
    if d != -1:
        return DOWN
    elif r != -1:
        return RIGHT
    elif l != -1:
        return LEFT
    elif u != -1:
        return UP

def score(cells):
    return score_recurse(cells, 2)

def score_individual(cells):
    return (10 * score_free_moves(cells) +
            10 * score_empties(cells) +
            score_max(cells))

def score_max(cells):
    import math
    return math.log(max_value(cells))

def max_value(cells):
    max = 0
    for r in cells:
        for c in r:
            if c > max:
                max = c
    return max

def score_empties(cells):
    n = 0
    for r in cells:
        for c in r:
            if c == 0:
                n += 1
    return n / 16.0

def score_free_moves(cells):
    l_copy, r_copy, u_copy, d_copy = all_boards(cells)
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

def score_recurse(cells, n):
    l_copy, r_copy, u_copy, d_copy = all_boards(cells)
    if n == 0:
        l = score_individual(l_copy)
        r = score_individual(r_copy) + 1
        u = score_individual(u_copy)
        d = score_individual(d_copy) + 1
    else:
        l = score_individual(l_copy)
        r = score_recurse(r_copy, n - 1)
        u = score_individual(u_copy)
        d = score_recurse(d_copy, n - 1)
    return max([l, r, u, d])

