from board import *

def simple_board():
    b = Board()
    b.cell_store = [
        [0, 0, 0, 0],
        [0, 3, 3, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        ]
    return b

def simple_board_down():
    b = Board()
    b.cell_store = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 3, 3, 0],
        [0, 0, 0, 0],
        ]
    return b

def simple_board_left():
    b = Board()
    b.cell_store = [
        [0, 0, 0, 0],
        [3, 3, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        ]
    return b

def simple_board_right():
    b = Board()
    b.cell_store = [
        [0, 0, 0, 0],
        [0, 0, 3, 3],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        ]
    return b

def simple_board_up():
    b = Board()
    b.cell_store = [
        [0, 3, 3, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        ]
    return b

def ugly_board():
    b = Board()
    b.cell_store = [
        [1, 12, 0, 0],
        [48, 3,  3, 6],
        [2, 6,  0, 0],
        [1, 1,  1, 12],
        ]
    return b

def jammed_board():
    b = Board()
    b.cell_store = [
        [1, 12,  1, 2],
        [48, 3,  1, 6],
        [2,  6,  1, 1],
        [3,  1,  1, 12],
        ]
    return b

def nice_board():
    b = Board()
    b.cell_store = [
        [1, 0, 0, 0],
        [0, 3,  3, 6],
        [2, 6,  0, 12],
        [1, 3,  0, 48],
        ]
    return b
