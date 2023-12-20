from board import Board
from player import Player
from cli import print_board, print_winner, print_draw

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player('X'), Player('O')]
        self.current_player_index = 0

    def start(self):
        while not self.board.is_full() and not self.board.has_winner():
            print_board(self.board)
            self.make_move()
            self.switch_player()

        print_board(self.board)
        if self.board.has_winner():
            print_winner(self.current_player())
        else:
            print_draw()

    def make_move(self):
        player = self.current_player()
        move_made = False
        while not move_made:
            try:
                move = player.get_move(self.board)
                self.board.make_move(move, player.symbol)
                move_made = True
            except ValueError as e:
                print(e)

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def current_player(self):
        return self.players[self.current_player_index]