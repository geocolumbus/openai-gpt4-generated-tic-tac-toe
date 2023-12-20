def print_help():
    help_text = (
        "Tic Tac Toe Game\n"
        "Usage:\n"
        "  python main.py: Start a new game\n"
        "  python main.py -h: Show this help message\n"
        "\n"
        "During the game, enter your move as 'row,col' when prompted.\n"
        "Rows and columns are 0-indexed."
    )
    print(help_text)

def print_board(board):
    for row in board.board:
        print(' | '.join(row))
        print('-' * 5)

def print_winner(player):
    print(f"Player {player.symbol} wins!")

def print_draw():
    print("It's a draw!")