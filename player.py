import random

class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.move = None

    def get_move(self):
        return self.move



class CPU(Player):

    def __init__(self):
        super().__init__() 

    def get_move(self):
        random_item = random.choice(list)
        return random_item
    


class Human(Player):

    def __init__(self) -> None:
        super().__init__()

    def get_move(self):
        while True:
            user_move = input("Enter your move: ").lower()
            if user_move in moves:
                self.move = user_move
                break
            print("Invalid move. Please try again.")

    