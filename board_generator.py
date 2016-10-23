from consts import *
import board

class BoardGenerator(object):
    def __init__(self, board):
        self.board = board

    def all_boards(self):
        boards = {}
        boards[LEFT]  = board.Board(self.board)
        boards[RIGHT] = board.Board(self.board)
        boards[UP]    = board.Board(self.board)
        boards[DOWN]  = board.Board(self.board)
        return boards
