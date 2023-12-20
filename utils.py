def check_win(board, symbol):
    for row in board.board:
        if all(s == symbol for s in row):
            return True
    for col in zip(*board.board):
        if all(s == symbol for s in col):
            return True
    if all(board.board[i][i] == symbol for i in range(3)):
        return True
    if all(board.board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(all(cell != ' ' for cell in row) for row in board.board)