import argparse
import threes_strategy
from keyboard_strategy import *
from recurse_strategy import *
from random_strategy import *
from consts import *
from board import *
from getch import *

parser = argparse.ArgumentParser()
parser.add_argument("--strategy", 
                    default="keyboard",
                    help="Name of the strategy you want to use.")
parser.add_argument("--depth",
                    default=3,
                    help="Recurse depth")
parser.add_argument("--num_trials",
                    default=3,
                    help="Recurse depth")
parser.add_argument("--wait",
                    default=0,
                    help="wait each keypress on iteration")

def one_game(strategy, depth=2, wait=False):
    board = Board()
    strategy_instance = strategy(board, depth)
    strategy_instance.wait = wait
    while True:
        dir = strategy_instance.get_next_move()
        if dir == None:
            return board
        else: board.move(dir)

def play_all_games(strategy, num_trials=1, depth=2, wait=False):
    score_tot = 0
    for i in range(num_trials):
        board = one_game(strategy, depth, wait)
        print board
        score_tot += board.max_value()
    print score_tot / num_trials

if __name__ == '__main__':
    args = parser.parse_args()
    if args.strategy == "keyboard":
        one_game(KeyboardStrategy)
    elif args.strategy == "recurse":
        play_all_games(RecurseStrategy, int(args.num_trials), args.depth, int(args.wait))
    elif args.strategy == "random":
        play_all_games(RandomStrategy, int(args.num_trials))
    else: print "ERROR: Unknown strategy"
