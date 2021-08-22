# import libraries to be used within the player classes
import random
import math


class BasePlayer:
    """
    define a class for the user as the player
    """
    def __init__(self, tag):
        # tag stands for cross or nought
        self.tag = tag

    def get_move(self, game):
        pass


class Computer(BasePlayer):
    """
    random computer player class, built on top of BasePlayer superclass
    """

    def __init__(self, tag):
        super().__init__(tag)

    def get_move(self, game):
        # chooses a random available spot for their next move
        square = random.choice(game.available_moves())


class UserPlayer(BasePlayer):
    """
    player class for the user to play as, built on top of BasePlayer superclass
    """

    def __init__(self, tag):
        super().__init__(tag)

    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.tag + '\'s turn. Input move (0-8):')
            # checking whether value is an integer ensures the user has input a valid number # noqa
            # also checks whether the spot is available or not
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return value
