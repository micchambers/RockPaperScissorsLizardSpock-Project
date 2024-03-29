# (5 points): As a developer, I want to make at least 10 commits with descriptive messages.
# (15 points): As a developer, I want to find a way to properly incorporate inheritance into my game.
# (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and re-obtained if necessary.
# (10 points): As a developer, I want to store all of the gesture options/choices in a List (AS STRINGS). I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc).
# (10 points): As a player, I want the correct player to win a given round based on the choices made by each player.  See below for game rules!
# (10 points): As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner. 
# (10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.

# Rock crushes Scissors
# Scissors cuts Paper 
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock

from player import Human
from player import CPU
from game import Game

moves = ["rock", "paper", "scissors", "lizard", "spock"]

winning_moves = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"]
}

# p1 = Human("P1")

# p2 = Human("P2")

# computer = CPU()

# rpsls = Game()

# rpsls.game_start() 