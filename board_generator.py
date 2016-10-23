from consts import *
import board

class BoardGenerator(object):
    def __init__(self, board):
        self.board = board

    def all_boards(self):
        boards = {}
        boards[LEFT]  = board.Board(self.board).move(LEFT)
        boards[RIGHT] = board.Board(self.board).move(RIGHT)
        boards[UP]    = board.Board(self.board).move(UP)
        boards[DOWN]  = board.Board(self.board).move(DOWN)
        return boards
