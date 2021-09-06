from players import UserPlayer, ComputerPlayer, GeniusComputerPlayer
from colorama import Fore
import time


class NoughtsAndCrosses:
    """
    A class to define the game's structure:
        Game board
        Display board
        Make a move with a tag
        Validate the move
        Check whether last move is a winning move
    ...

    Methods
    -------
    print_board(self)
        Prints out the game board to the terminal.

    print_board_nums()
        Prints out numbers corresponding to the empty spaces
        which the user will be making a move to.

    available_moves(self)
        Appends an index to an empty list IF the spot is empty
        and validates the move if the spot is empty.

    empty_squares(self)
        Returns/keeps track of all empty squares throughout the game.

    make_move(self, square, tag)
        Places the user's and the computer's tags according to the index provided.
        If the index is an empty square, return True and make the move.
        If the index is occupied, return False and invalidate the move.

    winner(self, square, tag)
        Checks whether the previous move was a winning move.
        If so, return True and exit, otherwise, return False and keep the game going  # noqa
    """

    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 game board
        self.current_winner = None  # track the winner

# code credit: help on how to print a game board to the terminal was taken from https://stackoverflow.com/questions/44269612/python-drawing-a-tic-tac-toe-board  # noqa
# and from: https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874  # noqa

    def print_board(self):
        print('')
        print("Available Moves       Game Board")
        for num, row in enumerate([self.board[i*3:(i+1)*3] for i in range(3)]):
            availableMoves = self.available_moves_display()
            availableRow = availableMoves[num*3:(num+1)*3]
            availablePart = '| ' + ' | '.join(availableRow) + ' |'
            boardPart = '       | ' + ' | '.join(row) + ' |'
            print(availablePart + boardPart)

    @staticmethod
    def print_board_nums():
        """
        Tells us which number corresponds to each empty space
        i.e. 1 | 2 | 3 etc.
        """
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]  # noqa
        for row in number_board:
            numered_board = '| ' + ' | '.join(row) + ' |'
            print(numered_board)

        print('')

# end credit

    def available_moves_display(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(str(i))
            else:
                moves.append(' ')
        return moves

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
                print('')  # emprty line

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
    print(Fore.YELLOW + "███████████████████████████████████████")
    print("█                                     █")
    print("█   ▄▄█▄▄█▄▄   " + Fore.BLUE + "NOUGHTS" + Fore.YELLOW + "                █")  # noqa
    print("█   ▄▄█▄▄█▄▄       &                  █")
    print("█   " + Fore.RED + "X" + Fore.YELLOW + " █  █ " + Fore.BLUE + "O" + Fore.YELLOW + "       " + Fore.RED + "CROSSES" + Fore.YELLOW + "            █")  # noqa
    print("█                                     █")
    print("█                    BY GABRIEL ALVES █")
    print("███████████████████████████████████████\n")
    # end credit
    time.sleep(2)

    print("Welcome to " + Fore.BLUE + "Noughts" + Fore.YELLOW + " & " + Fore.RED + "Crosses" + Fore.YELLOW + "!")  # noqa

    time.sleep(2)

    while True:
        user = input("Please enter a username: \n")
        if len(user.strip()) == 0:
            print("Invalid username")
            continue
        else:
            break

    time.sleep(2)

    print(f"Hello {user}!")

    time.sleep(2)

    # code credit: help from https://stackoverflow.com/questions/42091015/check-if-python-input-contains-a-specific-word/42091192 # noqa
    while True:
        difficulty = input("Please select a difficulty to continue. Type in 'easy', 'hard' or 'quit' to exit: \n").strip().lower()  # noqa
        time.sleep(2)
        if difficulty == 'easy':
            print(f"You've selected {difficulty}, good luck!\n")
            run_easy_game()
        elif difficulty == 'hard':
            print(f"You've selected {difficulty}, try your hardest to beat the computer!\n")  # noqa
            run_hard_game()
        elif difficulty == 'quit':
            print(f"Thanks for playing {user}, goodbye!")
            break
        else:
            print("You need to enter a valid difficulty to continue...\n")
            continue
    # end credit


intro()
