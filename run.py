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

def read_int(prompt: str, min_value: int = 1, max_value: int = 5) -> int:
    """
    Read an integer from user input.
    """

    while True:
        number = input(prompt)
        try:
            value = int(number)
            if value < min_value:
                print(f"The minimum value is {min_value}. Try again.")
            elif value > max_value:
                print(f"The maximum value is {max_value}. Try again.")
            else:
                return value
        except ValueError:
            print("That's not a number! Try again.")

            
class BattleshipBoard:
    """
    This class represents the game board for the Battleship game,
    It initializes the board and randomly places a single ship on it.
    Checks if there is a ship at the specified row and column.
    Checks if the specified cell has already been guessed.
    It places a guess on the specified cell.
    """
    
    def __init__(self, size_x: int, size_y: int) -> None:
        
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


def read_guess(already_guessed: Callable[[int, int], bool]) -> tuple[int, int]:
    """
    Read and valid guess from the player.
    """

    while True:
        # read the row and column
        guess_row = read_int("Guess row: ", max_value=BOARD_SIZE_Y) - 1
        guess_col = read_int("Guess column: ", max_value=BOARD_SIZE_X) - 1

        # if the guess is valid, return the guessed row and column
        if not already_guessed(guess_row, guess_col):
            return guess_row, guess_col

        print("You've already guessed on that row! Try again.")


def turn(board: BattleshipBoard) -> bool:
    """
    Responsible for handling a single player's turn in the game.
    """

    print(board.to_string())

    # let the player guess
    guess_row, guess_col = read_guess(board.already_guessed)
    board.place_guess(guess_row, guess_col)

    # if you found the ship, you win
    return board.is_ship(guess_row, guess_col)

def main() -> None:
    os.system("clear")

    print('--'*34)
    print(' WELCOME to The Battleship Game! \n The board size is 5x5,')
    print(' From the top left conor you have row = 1 and column = 1 ')
    print(' You can either have 1 player or 2 player and each one has 5 guesses')
    print('--'*34)


    player_count = read_int(
        "Please enter how many players are going to play: ", max_value=2
    )
    board = BattleshipBoard(BOARD_SIZE_X, BOARD_SIZE_Y)
    


if __name__ == "__main__":
    main()




