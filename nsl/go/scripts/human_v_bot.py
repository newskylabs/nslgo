## =========================================================
## human_v_bot.py
## ---------------------------------------------------------

import time

from nsl.go import agent
# Import goboard 
# There are three versions with different degree of optimizations:
#| from nsl.go import goboard_slow as goboard
from nsl.go import goboard
#| from nsl.go import goboard_fast as goboard
from nsl.go import gotypes
from nsl.go.utils import print_board, print_move, point_from_coords, clear_screen

## =========================================================
## Main
## ---------------------------------------------------------

def human_v_bot(board_size=9):
    """A human playing against a random bot.
    """

    game = goboard.GameState.new_game(board_size)
    bot = agent.RandomBot()

    while not game.is_over():

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
        
        # Calculate the next move
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)

        # Print the next move
        print_move(game.next_player, move)
        print('')
        
        # Apply the move
        game = game.apply_move(move)

## =========================================================
## =========================================================

## fin.
