from players import UserPlayer, ComputerPlayer, GeniusComputerPlayer
import time


class NoughtsAndCrosses:
    """
    create a game-board for the game to run on
    checks for available and invalid moves
    counts empty squares
    defines how to make moves
    defines winning moves
    """
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 game-board
        self.current_winner = None  # track the winner

    def print_board(self):
        # gets the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        """
        tells us which number corresponds to each empty space
        i.e. 1 | 2 | 3 etc.
        """
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]  # noqa
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, tag):
        """
        if the move is valid, proceed & return True
        if the move is invalid, returns False
        """
        if self.board[square] == ' ':
            self.board[square] = tag
            if self.winner(square, tag):
                self.current_winner = tag
            return True
        return False

    def winner(self, square, tag):
        """
        winner if player ticks 3 in a row (either vertically, horizontally, or diagonally) # noqa
        """

        # checks horizontally
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == tag for spot in row]):
            return True

        # checks vertically
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == tag for spot in column]):
            return True

        # checks diagonally
        # this is only possible if all squares are even numbers
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == tag for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == tag for spot in diagonal2]):
                return True

        # if all above fails
        return False


def play(game, x_player, o_player, print_game=True):
    """
    returns the winner of the game or None if it's a tie
    """
    if print_game:
        game.print_board_nums()

    tag = 'X'  # starting tag

    while game.empty_squares():
        """
        iterate as long as the game-board still has empty squares
        gets move from appropriate player
        """
        if tag == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, tag):
            if print_game:
                print(tag + f' makes a move to square {square}')
                game.print_board()
                print('')  # empty line

            if game.current_winner:
                if print_game:
                    print(tag + ' wins!')
                return tag

            # alternates / switches players for each round
            if tag == 'X':
                tag = 'O'
            else:
                tag = 'X'

        time.sleep(2)  # a break in between moves to make the game more user friendly # noqa
    if print_game:
        print('It\'s a tie!')


def run_easy_game():
    x_player = UserPlayer('X')
    o_player = ComputerPlayer('O')
    n_and_c = NoughtsAndCrosses()
    play(n_and_c, x_player, o_player, print_game=True)


def run_hard_game():
    x_player = UserPlayer('X')
    o_player = GeniusComputerPlayer('O')
    n_and_c = NoughtsAndCrosses()
    play(n_and_c, x_player, o_player, print_game=True)


def intro():
    # code credit: help from fellow slacker https://github.com/roomacarthur/escape-the-cave # noqa
    print("███████████████████████████████████████")
    print("█                                     █")
    print("█   ▄▄█▄▄█▄▄   NOUGHTS                █")
    print("█   ▄▄█▄▄█▄▄       &                  █")
    print("█   X █  █ O       CROSSES            █")
    print("█                                     █")
    print("█                    BY GABRIEL ALVES █")
    print("███████████████████████████████████████\n")
    # end credit
    print('Welcome to Noughts & Crosses!')

    # code credit: help from https://stackoverflow.com/questions/42091015/check-if-python-input-contains-a-specific-word/42091192 # noqa
    while True:
        difficulty = input("Please select a difficulty. Type in 'easy', 'hard' or 'quit' to exit: \n") # noqa
        if difficulty == 'easy':
            print(f"You've selected {difficulty}, good luck!\n")
            run_easy_game()
        elif difficulty == 'hard':
            print(f"You've selected {difficulty}, try your hardest to beat the computer!\n")  # noqa
            run_hard_game()
        elif difficulty == 'quit':
            print("Thanks for playing, goodbye!")
            break
        else:
            print("You need to enter a valid difficulty to continue...\n")
            continue
    # end credit


intro()
