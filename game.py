from player import Human
from player import CPU


class Game:
    def __init__ (self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def game_start():
        round_number = 1
        while round_number <= 3:
            print(f"Round {round_number}:")
            self.player1.get_move()
            self.player2.get_move()

