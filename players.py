import random
import math


class BasePlayer:
    """
    Base Player class to select a tag (either X or O) and a game.
    To be used as a superclass for the User, Computer
    and Genius Computer classes below.
    """

    def __init__(self, tag):
        self.tag = tag

    def get_move(self, game):
        pass


class ComputerPlayer(BasePlayer):
    """
    Random Computer Player class is used to define a computer
    for the user to play against.
    It makes its moves randomly according to what moves are available
    on the game board.
    ...

    Methods
    -------
    get_move(self, game)
        Makes a move to a random square according to game.available_moves()
    """

    def __init__(self, tag):
        super().__init__(tag)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class UserPlayer(BasePlayer):
    """
    User Player class defines the player the user will be playing as.
    It allows the user to make a move and then validates the move.
    ...

    Methods
    -------
    get_move(self, game)
        Loops through valid squares and continues for
        as long as the square is valid.
        If it is invalid, raises a ValueError and loops through again.
    """

    def __init__(self, tag):
        super().__init__(tag)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.tag + '\'s turn. Make a move:')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return val


# code credit: code for minimax algorithm taken from https://www.youtube.com/watch?v=8ext9G7xspg # noqa
class GeniusComputerPlayer(BasePlayer):
    """
    Genius Computer Player is a class to define an unbeatable
    computer player that uses a minimax algorithm to function.
    The algorithm maximizes its score whilst minimizing its losses,
    making it impossible to be beaten.
    ...

    Methods
    -------
    get_move(self, game)
        If the Genius computer is making the first move, choose it randomly,
        otherwise, use the algorithm to make a move.

    minimax(self, state, player)
        Keeps track of positions and score in dictionaries.
        Use algorithm to simulate a game after previous move.
        Update position and score dictionary.

    """
    def __init__(self, tag):
        super().__init__(tag)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # randomly choose one # noqa
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.tag)['position']
        return square

    def minimax(self, state, player):
        max_player = self.tag  # yourself
        other_player = 'O' if player == 'X' else 'X'  # the other player

        # firstly check whether the previous move was a winning move
        if state.current_winner == other_player:
            # we must keep track of position and score for minimax to work
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)  # noqa
            }
        elif not state.num_empty_squares():  # no empty squares left
            return {'position': None, 'score': 0}

        # initialize dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize  # noqa
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize  # noqa

        for possible_move in state.available_moves():
            # step 1: make a move
            state.make_move(possible_move, player)

            # step 2: use minimax algorithm to simulate a game after previous move  # noqa
            sim_score = self.minimax(state, other_player)  # alternate players

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step 4: update dictionaries if necessary
            if player == max_player:  # maximize max_player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:  # but minimize other_player
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
# end credit
