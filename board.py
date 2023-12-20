class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        print("┌───┬───┬───┐")
        for i, row in enumerate(self.board):
            print("│ " + " │ ".join(row) + " │")
            if i < 2:
                print("├───┼───┼───┤")
        print("└───┴───┴───┘")

    def make_move(self, position, symbol):
        x, y = position
        self.board[x][y] = symbol

    def is_position_empty(self, position):
        x, y = position
        return self.board[x][y] == ' '