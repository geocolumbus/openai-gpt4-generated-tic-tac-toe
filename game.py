from board import Board
from player import Player
from computer import Computer
from utils import check_win, check_draw

class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player('X')
        self.computer = Computer('O')
        self.current_turn = self.player

    def switch_turn(self):
        self.current_turn = self.computer if self.current_turn == self.player else self.player

    def play(self):
        while True:
            self.board.draw_board()
            move = self.current_turn.get_move(self.board)
            self.board.make_move(move, self.current_turn.symbol)

            if check_win(self.board, self.current_turn.symbol):
                self.board.draw_board()
                print(f"{self.current_turn.symbol} wins!")
                break
            elif check_draw(self.board):
                self.board.draw_board()
                print("It's a draw!")
                break

            self.switch_turn()