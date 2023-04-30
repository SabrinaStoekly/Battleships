import random

class Battleship:
    """
    Ses up the board  and places the  ship on a random possition 
    """
    def __init__(self):
        self.board = []
        self.ship_row = 0
        self.ship_col = 0
        self.num_turns = 0
        self.guesses = []

        for x in range(5):
            self.board.append(["-"] * 5)

        self.place_ship()

    def place_ship(self):
        self.ship_row = random.randint(0, 4)
        self.ship_col = random.randint(0, 4)

    def print_board(self):
        print("  1 2 3 4 5")
        for i, row in enumerate(self.board):
            print(i+1, " ".join(row))

game  = Battleship()
print(game.print_board())




