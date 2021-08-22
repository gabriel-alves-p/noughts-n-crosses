class NoughtsNCrosses:
    """
    create a game board for the game
    """
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 gameboard
        self.current_winner = None  # track the winner
    
    def print_board(self):
        # gets the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # tells us which number corresponds to each empty space
        # i.e. 1 | 2 | 3 etc.
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]  # noqa
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


