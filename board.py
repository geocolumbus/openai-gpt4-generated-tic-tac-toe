class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, move, symbol):
        if self.is_valid_move(move):
            self.board[move[0]][move[1]] = symbol
        else:
            raise ValueError("Invalid move")

    def is_valid_move(self, move):
        row, col = move
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def is_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def has_winner(self):
        # Check rows, columns, and diagonals for a winner
        lines = self.board + list(zip(*self.board)) + [self.diagonals()]
        return any(line.count(line[0]) == 3 and line[0] != ' ' for line in lines)

    def diagonals(self):
        return [self.board[i][i] for i in range(3)], [self.board[i][2 - i] for i in range(3)]