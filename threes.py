import copy, random

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

(LEFT, RIGHT, UP, DOWN) = range(4)

class Board(object):
    def __init__(self):
        self.cell_store = [[0,0,0,0],[3,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.next_queue = []
        self.next = self.pop_next_val()

    # Always move to the right. Just flip the board before doing
    # anything.
    # cells = transient. cell_store = permananent
    def move(self, direction):
        self.cell_store = self.transform(
            copy.deepcopy(self.cell_store), direction)

    def transform(self, cells, direction):
        cells = self.transpose(cells, direction)
        shifted = self.shift(cells)
        self.add(cells, shifted, self.next)
        self.next = self.pop_next_val()
        cells = self.restore(cells, direction)
        return cells

    def pop_next_val(self):
        if len(self.next_queue) == 0:
            self.next_queue = self.gen_next_queue()
        return self.next_queue.pop()

    def peek_next_val(self):
        return self.next

    def gen_next_queue(self):
        base = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
        random.shuffle(base)
        return base

    def transpose(self, new_cells, direction):
        if direction in [UP, DOWN]:
            new_cells = [list(a) for a in zip(*new_cells)]
        if direction in [LEFT, UP]:
            new_cells[0].reverse()
            new_cells[1].reverse()
            new_cells[2].reverse()
            new_cells[3].reverse()
        return new_cells

    def restore(self, new_cells, direction):
        if direction in [LEFT, UP]:
            new_cells[0].reverse()
            new_cells[1].reverse()
            new_cells[2].reverse()
            new_cells[3].reverse()
        if direction in [UP, DOWN]:
            new_cells = [list(a) for a in zip(*new_cells)]
        return new_cells

    # Mutates cells so they are shifted / merged to the right
    # Returns an array of rows that were shifted.
    def shift(self, cells):
        shifted = [True, True, True, True]
        for i, row in enumerate(cells):
            if (row[2] == row[3] and row[3] > 2 or
                row[2] == 1 and row[3] == 2 or
                row[2] == 2 and row[3] == 1 or
                row[2] != 0 and row[3] == 0):
                row[3] += row[2]
                row[2] = row[1]
                row[1] = row[0]
                row[0] = 0
            elif (row[1] == row[2] and row[2] > 2 or
                  row[1] == 1 and row[2] == 2 or
                  row[1] == 2 and row[2] == 1 or
                  row[1] != 0 and row[2] == 0):
                row[2] += row[1]
                row[1] = row[0]
                row[0] = 0
            elif (row[0] == row[1] and row[1] > 2 or
                  row[0] == 1 and row[1] == 2 or
                  row[0] == 2 and row[1] == 1 or
                  row[0] != 0 and row[1] == 0):
                row[1] += row[0]
                row[0] = 0
            else:
                shifted[i] = False
        return shifted

    def add(self, cells, shifted, next_val=3):
        rows = []
        for s, row in zip(shifted, cells):
            if s:
                rows.append(row)
        
        if len(rows) == 0: return
        tgt_row = random.randint(0, len(rows) - 1)
        rows[tgt_row][0] = next_val

    def __str__(self):
        r = ""
        r += "\t".join(map(str, self.cell_store[0])) + "\n"
        r += "\t".join(map(str, self.cell_store[1])) + "\n"
        r += "\t".join(map(str, self.cell_store[2])) + "\n"
        r += "\t".join(map(str, self.cell_store[3])) + "\n"
        return r

def get_move_direction(board):
    l_copy, r_copy, u_copy, d_copy = all_boards(board.cell_store)

    l = score(l_copy)
    if l_copy == board.cell_store:
        l = -1
    r = score(r_copy)
    if r_copy == board.cell_store:
        r = -1
    u = score(u_copy)
    if u_copy == board.cell_store:
        u = -1
    d = score(d_copy)
    if d_copy == board.cell_store:
        d = -1

    if u == d == r == l == -1:
        return None

    dir = LEFT
    max = l
    if u > max:
        max = u
        dir = UP
    if r > max:
        max = r
        dir = RIGHT
    if d > max:
        max = d
        dir = DOWN
#    return direction_override(l, r, u, d)
#    print l, r, u, d
    return dir

# LRUD
def all_boards(cells):
    b = Board()
    l_copy = b.transform(copy.deepcopy(cells), LEFT)
    r_copy = b.transform(copy.deepcopy(cells), RIGHT)
    u_copy = b.transform(copy.deepcopy(cells), UP)
    d_copy = b.transform(copy.deepcopy(cells), DOWN)
    return (l_copy, r_copy, u_copy, d_copy)

def direction_override(l, r, u, d):
    if d != -1:
        return DOWN
    elif r != -1:
        return RIGHT
    elif l != -1:
        return LEFT
    elif u != -1:
        return UP

def score(cells):
    return score_recurse(cells, 4)

def score_individual(cells):
    return (10 * score_free_moves(cells) +
            10 * score_empties(cells) +
            score_max(cells))

def score_max(cells):
    import math
    max = 0
    for r in cells:
        for c in r:
            if c > max:
                max = c
    return math.log(max)

def score_empties(cells):
    n = 0
    for r in cells:
        for c in r:
            if c == 0:
                n += 1
    return n / 16.0

def score_free_moves(cells):
    l_copy, r_copy, u_copy, d_copy = all_boards(cells)
    free_moves = 0
    if cells != l_copy:
        free_moves += 1
    if cells != r_copy:
        free_moves += 1
    if cells != u_copy:
        free_moves += 1
    if cells != d_copy:
        free_moves += 1
    return free_moves / 4.0

def score_recurse(cells, n):
    l_copy, r_copy, u_copy, d_copy = all_boards(cells)
    if n == 0:
        l = score_individual(l_copy)
        r = score_individual(r_copy)
        u = score_individual(u_copy)
        d = score_individual(d_copy)
    else:
        l = score_individual(l_copy)
        r = score_recurse(r_copy, n - 1)
        u = score_individual(u_copy)
        d = score_recurse(d_copy, n - 1)
    return max([l, r, u, d])

def print_recommendation(cells):
    l_copy, r_copy, u_copy, d_copy = all_boards(cells)
    l = score_individual(l_copy)
    r = score_individual(r_copy)
    u = score_individual(u_copy)
    d = score_individual(d_copy)
    print "Left", l
    print "Right", r
    print "Up", u
    print "Down", d

def main_key():
    board = Board()

    while True:
        print board
        print_recommendation(board.cell_store)
        print "NEXT: " + str(board.next)
        c = getch()
        if c == "q": break
        elif c == "w": board.move(UP)
        elif c == "a": board.move(LEFT)
        elif c == "s": board.move(DOWN)
        elif c == "d": board.move(RIGHT)

board_deb = None
dir_deb = None
def ai_trial():
    global board_deb, dir_deb
    board = Board()
    while True:
#        print board
#        print "NEXT: " + str(board.next)
#        c = getch()
#        if c == "q": break
        board_deb = board
        dir = dir_deb = get_move_direction(board)
        if dir == None:
            return score_max(board.cell_store)
        else:
#            print ["left", "right", "up", "down"][dir]
            board.move(dir)
        
def main_ai():
    num_trials = 1
    score_tot = 0
    for i in range(num_trials):
        score_tot += ai_trial()
    print score_tot / num_trials

if __name__ == '__main__':
    main_key()
#    try:
#        main_ai()
#    except:
#        print ""
#        print board_deb.cell_store
#        print ["left", "right", "up", "down"][dir_deb]
