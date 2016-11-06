import unittest
from test_boards import *
from board_generator import *
from consts import *

class TestBoard(unittest.TestCase):

    def test_eq(self):
        b = simple_board()
        b2 = simple_board()
        self.assertEqual(b, b2)

    def test_not_eq(self):
        b = simple_board()
        b2 = simple_board()
        b2.move(LEFT)
        self.assertNotEqual(b, b2)

    def test_eq_different_queue(self):
        b = Board()
        b2 = Board(b)
        b2.next = 7
        self.assertEqual(b, b2)

    def test_board_move_right(self):
        b = right_board()
        b.move(RIGHT)
        self.assertEqual(b.cell_store[3][3], 24)


if __name__ == '__main__':
    unittest.main()
