class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        move = input(f"Player {self.symbol}, enter your move (row,col): ")
        return tuple(map(int, move.strip().split(',')))