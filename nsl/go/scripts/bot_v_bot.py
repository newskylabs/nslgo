## =========================================================
## bot_v_bot.py
## ---------------------------------------------------------

import time

from nsl.go import agent
from nsl.go import goboard_slow as goboard
from nsl.go import gotypes
from nsl.go.utils import print_board, print_move, clear_screen

## =========================================================
## Main
## ---------------------------------------------------------

def bot_v_bot(board_size=9, sleep=0.3):
    """A random bot playing against another random bot.
    """
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }
    while not game.is_over():

        # We set a sleep timer to 0.3 seconds so that bot moves aren't
        # printed too fast to observe
        time.sleep(sleep)

        # Before each move we clear the screen. This way the board is
        # always printed to the same position on the command line.
        #| print(chr(27) + "[2J")
        clear_screen()

        # Print a header
        print('')
        print('  nslgo')
        print('')

        # Print the board
        print_board(game.board)
        print('')
        
        # Calculate and print the next move
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        print('')
        
        # Apply the move
        game = game.apply_move(bot_move)

## =========================================================
## =========================================================

## fin.
