import random
import math


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
            square = input(self.tag + '\'s turn. Make a move (0-8):')
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
