import sys
from game import Game
from cli import print_help

def main():
    if "-h" in sys.argv:
        print_help()
    else:
        game = Game()
        game.start()

if __name__ == "__main__":
    main()