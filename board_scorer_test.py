import unittest
from consts import *
from board import *
from board_scorer import *
from test_boards import *

class TestBoardScorer(unittest.TestCase):

    def test_count_inversions_simple(self):
        r = BoardScorer(simple_board())
        self.assertEquals(1.0 / 3, r.inversions())

    def test_count_inversions_ugly(self):
        r = BoardScorer(ugly_board())
        self.assertEquals(1.0 / 9, r.inversions())

    def test_count_inversions_nice(self):
        r = BoardScorer(nice_board())
        self.assertEquals(1.0 / 7, r.inversions())

    def test_free_moves_simple(self):
        r = BoardScorer(simple_board())
        self.assertEquals(1.0, r.free_moves())

    def test_free_moves_ugly(self):
        r = BoardScorer(ugly_board())
        self.assertEquals(1.0, r.free_moves())

    def test_free_moves_jammed(self):
        r = BoardScorer(jammed_board())
        self.assertEquals(0.5, r.free_moves())

    def test_free_moves_nice(self):
        r = BoardScorer(nice_board())
        self.assertEquals(1.0, r.free_moves())


if __name__ == '__main__':
    unittest.main()

