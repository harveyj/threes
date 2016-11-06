import random, copy
from consts import *

class Board(object):
    def __init__(self, brd=None):
        self.next_queue = []
        if brd:
            self.cell_store = copy.deepcopy(brd.cell_store)
            self.next = brd.next
            self.next_queue = copy.deepcopy(brd.next_queue)
            random.shuffle(self.next_queue)
        else:
            self.cell_store = [[0,0,0,0],[3,0,0,0],[0,0,0,0],[0,0,0,0]]
            self.next = self.pop_next_val()


    def __str__(self):
        r = ""
        r += "\t".join(map(str, self.cell_store[0])) + "\n"
        r += "\t".join(map(str, self.cell_store[1])) + "\n"
        r += "\t".join(map(str, self.cell_store[2])) + "\n"
        r += "\t".join(map(str, self.cell_store[3])) + "\n"
        return r

    def __eq__(self, brd):
        return self.cell_store == brd.cell_store

    def __ne__(self, brd):
        return not self.__eq__(brd)

    # Always move to the right. Just flip the board before doing
    # anything.
    # cells = transient. cell_store = permananent
    def move(self, direction):
        self.cell_store = self.transform(
            copy.deepcopy(self.cell_store), direction)
        return self

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

    def max_value(self):
        max = 0
        for r in self.cell_store:
            for c in r:
                if c > max:
                    max = c
        return max
