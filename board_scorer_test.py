import unittest
from consts import *
from board import *
from board_scorer import *

class TestBoardScorer(unittest.TestCase):

    def test_count_inversions(self):
        b = Board()
        b.cell_store = [
            [0, 0, 0, 0],
            [0, 3, 3, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            ]
        r = BoardScorer(b)
        self.assertEquals(3, r.count_inversions())

if __name__ == '__main__':
    unittest.main()

