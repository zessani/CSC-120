"""
    File: battleship.py
    Author: Zayyan Essani
    Course: CSC 120, Spring 2024
    Purpose: This program writes a program to model
            half of the battleship game using a 10x10 grid.
            Player one places ships and player 2 guesses.
"""

import sys

class GridPos:
    """
    This class represents the grid position

    The class defines the methods for defining the GridPos
    object and the methods to return/print the object

    """
    def __init__(self, x, y):
        """
        Initializes a GridPos object by setting the
        coordinates, char and ship type.

        Parameters:
            x,y: integer coordinates
        
        Returns: None
            
        """
        self._x = x
        self._y = y
        self._char = '.'
        self._ship = None

    def __str__(self):
        if self._ship is None:
            return "."
        return str(self._ship)

class Board:
    """
    This class represents the game board

    The class defines methods for initializing the game
    board, placing ships, and printing the board.

    """
    def __init__(self):
        """
        Initializes a Board object by creating a 10x10
        grid of GridPos objects.

        Parameters:None
        
        Returns: None
            
        """
        self._outer = []
        for i in range(10):
            inner = []
            for j in range(10):
                inner.append(GridPos(j, i))
            self._outer.append(inner)

    def place_one_ship(self, placement_list):
        """
        Places a single ship on the board.

        Parameters:
            placement_list: A string containing ship placement information
        
        Returns: None
        """
        string = "".join(placement_list.split())
        kind = string[0]
        x1 = int(string[1])
        y1 = int(string[2])
        x2 = int(string[3])
        y2 = int(string[4])
        ship = Ship(kind, x1, y1, x2, y2)
        # If ship is horizontal
        if (y1 - y2) == 0:
            if x1 < x2:
                for i in range(x1, x2 + 1):
                    self._outer[i][y1]._ship = ship
            else:
                for i in range(x2, x1 + 1):
                    self._outer[i][y1]._ship = ship
        # If ship is vertical
        elif (x1 - x2) == 0:
            if y1 < y2:
                for i in range(y1, y2 + 1):
                    self._outer[x1][i]._ship = ship
            else:
                for i in range(y2, y1 + 1):
                    self._outer[x1][i]._ship = ship

    def __str__(self):
        for i in range(9, -1, -1):
            # print GridPos objects
            for j in range(10):
                print(self._outer[j][i], end="")
            print()

class Ship:
    """
    This class represents a ship.

    The class defines methods for initializing a ship,
    calculating its size, positions, and updating hits.
    """
    def __init__(self, kind, x1, y1, x2, y2):
        """
        Initializes a Ship object by setting its kind,
        hit points, and coordinates.
.
        Parameters:x1, y1, x2, y2: x and y coordinates
        
        Returns: None
            
        """
        self._kind = kind
        self._hit = self.ship_size()
        self._cords = None
        self.ship_positions(x1, y1, x2, y2)

    def ship_size(self):
        """
        Calculates the size of the ship based on its kind.

        Parameters: None
        
        Returns:
            int: The size of the ship
        """
        if self._kind == "A":
            return 5
        elif self._kind == "B":
            return 4
        elif self._kind == "S":
            return 3
        elif self._kind == "D":
            return 3
        elif self._kind == "P":
            return 2

    def ship_positions(self, x1, y1, x2, y2):
        """
        Calculates the positions occupied by the ship.
.
        Parameters:x1, y1, x2, y2: x and y coordinates
        
        Returns: None
            
        """
        grid = []
        if (y1 - y2) == 0:
            for i in range(x1, x2 + 1):
                grid.append([i, y1])
        elif (x1 - x2) == 0:
            for i in range(y1, y2 + 1):
                grid.append([x1, i])
        self._cords = grid

    def one_hit(self):
        """
        Updates the hit points of the ship after being hit once.

        Parameters: None
        
        Returns: None
        """
        self._hit = int(self._hit) - 1

    def __str__(self):
        return str(self._kind)


def error_checks(placement_list):
    """
    Checks for errors in the ship placements.

    Parameters:
        placement: A list of ship placements
        
    Returns: None
    """
    kinds = ['A', 'B', 'S', 'D', 'P']
    for i in placement_list:
        for j in kinds:
            if str(i[0]) == j:
                kinds.pop(kinds.index(j))
    if len(kinds) != 0:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)
    elif len(placement_list) > 5:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)
    else:
        overlap_list = []
        for j in placement_list:
            i = j.split(" ")
            kind = str(i[0])
            x1 = int(i[1])
            y1 = int(i[2])
            x2 = int(i[3])
            y2 = int(i[4])
            # Check if ship is within bounds
            if (x1 < 0) or (x1 > 9) or (y1 < 0) or (y1 > 9)\
                    or (x2 < 0) or (x2 > 9) or (y2 < 0) or (y2 > 9):
                print("ERROR: ship out-of-bounds: " + j)
                sys.exit(0)
            # Check if ship is horizontal or vertical
            if (x1 - x2) != 0 and (y1 - y2) != 0:
                print("ERROR: ship not horizontal or vertical: " + j)
                sys.exit(0)
            ship = Ship(kind, x1, y1, x2, y2)
            for position in ship._cords:
                # check if ships are overlapping
                if position not in overlap_list:
                    overlap_list.append(position)
                else:
                    print("ERROR: overlapping ship: " + j)
                    sys.exit(0)
            if (x1 - x2) == 0:
                # check if it is the expected size
                if abs(y1 - y2) + 1 != ship.ship_size():
                    print("ERROR: incorrect ship size: " + j)
                    sys.exit(0)
            elif (y1 - y2) == 0:
                # Check if ship size matches the expected size for its kind
                if abs(x1 - x2) + 1 != ship.ship_size():
                    print("ERROR: incorrect ship size: " + j)
                    sys.exit(0)


def main():
    placement_file_name = input()
    guess_file_name = input()
    
    placement_file = open(placement_file_name, "r")
    guess_file = open(guess_file_name, "r")

    placement = placement_file.readlines()
    guesses = guess_file.readlines()

    error_checks(placement)
    board = Board()
    for j in placement:
        board.place_one_ship(j)
    miss_list = []
    for j in guesses:
        k = j.strip('\n')
        i = k.split(" ")
        if 0 <= int(i[0]) > 9 or 0 <= int(i[1]) > 9:
            print("illegal guess")
            continue
        coord = board._outer[int(i[0])][int(i[1])]
        if coord._ship is not None:
            if coord._ship._kind in "ASBDP":
                if coord._char != "x":
                    coord._ship.one_hit()
                    if coord._ship._hit == 0:
                        print(coord._ship._kind, "sunk")
                    else:
                        print("hit")
                    coord._char = "x"
                else:
                    print("hit (again)")
        else:
            # Check if the guessed position has already been missed
            if board._outer[int(i[0])][int(i[1])] not in miss_list:
                print("miss")
                miss_list.append(board._outer[int(i[0])][int(i[1])])
            else:
                print("miss (again)")

    placement_file.close()
    guess_file.close()
    print("all ships sunk: game over")


main()
