import random

class Computer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        empty_positions = [(x, y) for x in range(3) for y in range(3) if board.is_position_empty((x, y))]
        return random.choice(empty_positions)