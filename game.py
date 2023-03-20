from player import Human
from player import CPU

moves = ["rock", "paper", "scissors", "lizard", "spock"]

winning_moves = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"]
}

class Game:
    def __init__ (self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def game_start(self):
        self.active = True
        round_number = 3
        print(F"Rock, Paper, Scissors, Lizard, Spock.\n {self.player1.name} vs {self.player2.name}\n")
        while self.active == True:
            print(f"Round {round_number}:\n")
            self.player1.get_move()
            self.player2.get_move()
            round_number -= 1
            if self.player1.move == self.player2.move:
                print("Tie")
            elif self.player2.move in winning_moves[self.player1.move]:
                print(f"Point: {self.player1.name}")
            else:
                print(f"Point: {self.player1.name}")
            if round_number == 0:
                self.active == False
                if self.player1.score >= self.player2.score:
                    print(f"Win: {self.player1.name}")
                elif self.player2.score >= self.player1.score:
                    print(f"Win: {self.player2.name}")
                else:
                    print("The game was a tie.")
