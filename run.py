# Imports
import os
import random
from typing import Callable

#Constants used to represent the amount of guesses of each player
#and definy the size ofthe board 5x5
GUESSES_COUNT = 5
BOARD_SIZE_X = 5
BOARD_SIZE_Y = 5

# Constants used to represent elements on the board
HIDDEN = "-"
SHIP = "S"
GUESS = "X"


            
class BattleshipBoard:
    """
    This class represents the game board for the Battleship game,
    It initializes the board and randomly places a single ship on it.
    Checks if there is a ship at the specified row and column.
    Checks if the specified cell has already been guessed.
    It places a guess on the specified cell.
    """
    
    def __init__(self, size_x: int, size_y: int) -> None:
        # create the grid
        self.grid = [[HIDDEN] * size_x for _ in range(size_y)]

        # place a random ship on the grid
        ship_row = random.randint(0, size_y - 1)
        ship_col = random.randint(0, size_x - 1)
        self.grid[ship_row][ship_col] = SHIP

    def is_ship(self, row: int, col: int) -> bool:
        return self.grid[row][col] == SHIP

    def already_guessed(self, row: int, col: int) -> bool:
        return self.grid[row][col] == GUESS

    def place_guess(self, row: int, col: int) -> None:
        if not self.is_ship(row, col):
            self.grid[row][col] = GUESS

    def to_string(self, show_ship: bool = False) -> str:
        rows_str: list[str] = []
        for row in self.grid:
            row = [HIDDEN if col == SHIP and not show_ship else col.replace("0", HIDDEN) for col in row]
            rows_str.append(" ".join(row))
        return "\n".join(rows_str)





