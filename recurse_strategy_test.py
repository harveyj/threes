import unittest
from consts import *
from board import *
from recurse_strategy import *

class TestRecurseStrategy(unittest.TestCase):

    def test_right(self):
        return
        b = Board()
        b.cell_store = [
            [0, 0, 0, 0],
            [0, 3, 3, 0],
            [0, 0, 0, 3],
            [0, 0, 0, 0],
            ]
        r = RecurseStrategy(b)
        r.depth = 0
        self.assertEquals(DOWN, r.get_move_direction(b))

    def test_merge(self):
        b = Board()
        b.cell_store = [
            [0, 0, 0,  1],
            [0, 3, 1,  2],
            [0, 0, 0,  6],
            [0, 0, 12, 12],
            ]
        r = RecurseStrategy(b)
        r.depth = 1
        self.assertEquals(RIGHT, r.get_move_direction(b))

    def test_wtf(self):
        b = Board()

        b.cell_store = [
            [0, 3, 3, 3],
            [3, 2, 6, 6],
            [12, 6, 3, 12],
            [1, 3, 12, 3]
            ]
        r = RecurseStrategy(b)
        r.depth = 1
        print r.score_iter(b, 1)
        self.assertEquals("RIGHT", d(r.get_move_direction(b)))
    

if __name__ == '__main__':
    unittest.main()
