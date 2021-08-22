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
        pass


class UserPlayer(BasePlayer):
    """
    player class for the user to play as, built on top of BasePlayer superclass
    """

    def __init__(self, tag):
        super().__init__(tag)

    def get_move(self, game):
        pass
