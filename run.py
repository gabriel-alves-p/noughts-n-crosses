from players import UserPlayer, ComputerPlayer
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

    letter = 'X'  # starting tag

    while game.empty_squares():
        """
        iterate as long as the game-board still has empty squares
        gets move from appropriate player
        """
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # alternates / switches players for each round
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'

        time.sleep(3)
    if print_game:
        print('It\'s a tie!')


def main():
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)


main()
