## =========================================================
## bot_v_bot.py
## ---------------------------------------------------------

from nsl.go import agent
from nsl.go import goboard
from nsl.go import gotypes
from nsl.go.utils import print_board, print_move
import time

## =========================================================
## main()
## ---------------------------------------------------------

def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }
    while not game.is_over():

        # We set a sleep timer to 0.3 seconds so that bot moves aren't
        # printed too fast to observe
        time.sleep(0.3)

        # Before each move we clear the screen. This way the board is
        # always printed to the same position on the command line.
        print(chr(27) + "[2J")
        
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)

## =========================================================
## Main
## ---------------------------------------------------------

if __name__ == '__main__':
    main()

## =========================================================
## =========================================================

## fin.
