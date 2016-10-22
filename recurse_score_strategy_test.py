import unittest
from consts import *
from board import *
from recurse_score_strategy import *

class TestRecurseStrategy(unittest.TestCase):

    def test_right(self):
        b = Board()
        b.cell_store = [
            [0, 0, 0, 0],
            [0, 3, 3, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            ]
        r = RecurseStrategy(b)
        print r.get_move_direction(b)

if __name__ == '__main__':
    unittest.main()
