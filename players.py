import random


class BasePlayer:
    """
    define a class for the user as the player
    """

    def __init__(self, tag):
        self.tag = tag

    def get_move(self, game):
        pass


class ComputerPlayer(BasePlayer):
    """
    random computer player class, built on top of BasePlayer superclass
    """
    def __init__(self, tag):
        super().__init__(tag)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class UserPlayer(BasePlayer):
    """
    player class for the user to play as, built on top of BasePlayer superclass
    """
    def __init__(self, tag):
        super().__init__(tag)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.tag + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return val
