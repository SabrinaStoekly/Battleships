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

        


game  = Battleship()
print(game.board)



