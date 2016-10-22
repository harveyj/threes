from consts import *
import threes_strategy

# http://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
class _Getch:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

getch = _Getch()

class KeyboardStrategy(threes_strategy.Strategy):
    def __init__(self, board):
        super(KeyboardStrategy, self).__init__(board)

    def get_next_move(self):
        print self.board
        print "NEXT: " + str(self.board.next)

        c = getch()
        if c == "q": return None
        elif c == "w": return UP
        elif c == "a": return LEFT
        elif c == "s": return DOWN
        elif c == "d": return RIGHT

