from random import *
def init():
    grid_size = int(input())
    seed_value = input()
   
    seed(seed_value)
    return grid_size

def make_grid(grid_size):
    grid = []
    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            val = randint(ord('a'), ord('z'))
            letter = chr(val)
            row.append(letter)
        grid.append(row)
    return grid


def print_grid(grid):
    for row in grid:
        string = ""
        for i in range(len(row)):
            string += str(row[i])
            if i < len(row) - 1:
                string += ","
        print(string)

def main():
    grid_size = init()
    grid = make_grid(grid_size)
    print_grid(grid)

main()

