class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        while True:
            try:
                move = input("Enter your move (row,col): ")
                x, y = map(int, move.split(','))
                if board.is_position_empty((x, y)):
                    return x, y
                else:
                    print("This position is already taken.")
            except (ValueError, IndexError):
                print("Invalid move. Please enter row,col as two digits separated by a comma.")