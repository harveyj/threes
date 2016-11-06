import copy, math
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
        print (self.board.max_value(),
               self.board.cell_store[3][3] == self.board.max_value(),
               board_scorer.BoardScorer(self.board).combined())
        print d(dir)
        if self.wait:
            print self.board
            getch()
        return dir

    def get_move_direction(self, brd):
        path = self.score_iter(brd, self.depth)
        if path:
            return path[0]
        else: return None

    def score_individual(self, brd):
#        print '.',
        scorer = board_scorer.BoardScorer(brd)
        return scorer.combined()

    class PathBoard(object):
        def __init__(self, path, board):
            self.path = path
            self.board = board

    def score_iter(self, brd, n):
        pbs = [self.PathBoard([], brd)]
        for i in range(n):
            new_pbs = []
            for dir in [LEFT, RIGHT, UP, DOWN]:
                for p in pbs:
                    new_board = board.Board(p.board).move(dir)
                    if new_board != p.board:
                        new_pbs.append(self.PathBoard(p.path + [dir], new_board))
            pbs = new_pbs
        max_score = 0
        max_pb = None
        for p in pbs:
            s = self.score_individual(p.board)
            if p.path[0] in [DOWN, RIGHT]:
                s += 0.1
            if s > max_score:
                max_score = s
                max_pb = p
        return max_pb.path
