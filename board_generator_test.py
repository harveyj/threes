import unittest
from test_boards import *
from board_generator import *

class TestBoardGenerator(unittest.TestCase):

    def test_generator(self):
        b = simple_board()
        b.next = 3
        ab = BoardGenerator(b).all_boards()
        l_brd, r_brd, u_brd, d_brd = (ab[LEFT], ab[RIGHT], ab[UP], ab[DOWN])

        self.assertEquals(l_brd.cell_store[1][0], 3)
        self.assertEquals(l_brd.cell_store[1][1], 3)
        self.assertNotEquals(l_brd.cell_store[1][3], 0)

        self.assertEquals(r_brd.cell_store[1][2], 3)
        self.assertEquals(r_brd.cell_store[1][3], 3)
        self.assertNotEquals(r_brd.cell_store[1][0], 0)

        self.assertEquals(u_brd.cell_store[0][1], 3)
        self.assertEquals(u_brd.cell_store[0][2], 3)
        # Assert something got added

        self.assertEquals(d_brd.cell_store[2][1], 3)
        self.assertEquals(d_brd.cell_store[2][2], 3)
        # Assert something got added

if __name__ == '__main__':
    unittest.main()
