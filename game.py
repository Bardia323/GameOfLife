'''A simple Conway's Game of Life implementation in Python'''


import random
import time
import sys
import os
import argparse

from colorama import init, Fore, Back, Style
init()

# Define some colors
BLACK = Fore.BLACK + Back.BLACK
WHITE = Fore.WHITE + Back.WHITE
RED = Fore.RED + Back.RED
GREEN = Fore.GREEN + Back.GREEN
BLUE = Fore.BLUE + Back.BLUE
CYAN = Fore.CYAN + Back.CYAN
MAGENTA = Fore.MAGENTA + Back.MAGENTA
YELLOW = Fore.YELLOW + Back.YELLOW

# Define some constants
DEAD = 0
ALIVE = 1

# Define some globals
ROWS = 0
COLUMNS = 0
GENERATIONS = 0
DELAY = 0

# Define some structures
class cell:
    def __init__(self, state):
        self.state = state

class generation:
    def __init__(self, cells):
        self.cells = cells

# Define some functions
def init_generation(cells):
    for i in range(ROWS):
        cells.append([])
        for j in range(COLUMNS):
            cells[i].append(cell(DEAD))

def print_generation(cells):
    for i in range(ROWS):
        for j in range(COLUMNS):
            if cells[i][j].state == DEAD:
                print(BLACK + ' ', end='')
            else:
                print(WHITE + ' ', end='')
        print('')

def random_generation(cells):
    for i in range(ROWS):
        for j in range(COLUMNS):
            cells[i][j].state = random.randint(DEAD, ALIVE)

def next_generation(cells):
    new_cells = []
    init_generation(new_cells)
    for i in range(ROWS):
        for j in range(COLUMNS):
            state = cells[i][j].state
            live_neighbors = get_live_neighbors(cells, i, j)
            if state == DEAD and live_neighbors == 3:
                new_cells[i][j].state = ALIVE
            elif state == ALIVE and live_neighbors < 2:
                new_cells[i][j].state = DEAD
            elif state == ALIVE and (live_neighbors == 2 or live_neighbors == 3):
                new_cells[i][j].state = ALIVE
            elif state == ALIVE and live_neighbors > 3:
                new_cells[i][j].state = DEAD
    return new_cells

def get_live_neighbors(cells, row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i == row and j == col) or i < 0 or j < 0 or i >= ROWS or j >= COLUMNS:
                continue
            else:
                if cells[i][j].state == ALIVE:
                    count += 1
    return count

def get_args():
    parser = argparse.ArgumentParser(description='Conway\'s Game of Life')
    parser.add_argument('-r', '--rows', type=int, default=10, help='Number of rows')
    parser.add_argument('-c', '--columns', type=int, default=10, help='Number of columns')
    parser.add_argument('-g', '--generations', type=int, default=10, help='Number of generations')
    parser.add_argument('-d', '--delay', type=float, default=0.1, help='Delay between generations')
    args = parser.parse_args()
    return args

def main():
    global ROWS, COLUMNS, GENERATIONS, DELAY
    args = get_args()
    ROWS = args.rows
    COLUMNS = args.columns
    GENERATIONS = args.generations
    DELAY = args.delay

    cells = []
    init_generation(cells)
    random_generation(cells)
    print_generation(cells)

    for i in range(GENERATIONS):
        cells = next_generation(cells)
        print_generation(cells)
        time.sleep(DELAY)
        os.system('clear')

if __name__ == '__main__':
    main()