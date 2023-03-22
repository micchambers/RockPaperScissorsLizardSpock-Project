import random

moves = ["rock", "paper", "scissors", "lizard", "spock"]

winning_moves = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"]
}

class Player:

    def __init__(self):
        self.score = 0
        self.move = None

    def get_move(self):
        return self.move



class CPU(Player):

    def __init__(self):
        super().__init__()
        self.name = 'CPU'
        self.score = 0
        self.move = None

    def get_move(self):
        random_item = random.choice(moves)
        return random_item
    


class Human(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0
        self.move = None


    def get_move(self):
        self.user_move = input("Enter your move: \n").lower()
        if self.user_move in moves:
            self.move = self.user_move
        else:
            print("Invalid move.\n")
            return(self.get_move())

    