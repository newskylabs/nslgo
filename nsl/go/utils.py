## =========================================================
## nsl/go/utils.py
## ---------------------------------------------------------

import sys
import os

from nsl.go.__about__ import __version__
from nsl.go import gotypes

## =========================================================
## Version
## ---------------------------------------------------------

def get_version():
    """Return package version as defined in `setup.py` (ex: 1.2.3)."""

    return __version__

def get_version_long():
    """Return long package version (ex: 1.2.3 (Python 3.4.5))."""

    return '{} (Python {})'.format(get_version(), sys.version[:5])

## =========================================================
## COLS
## ---------------------------------------------------------

COLS = 'ABCDEFGHJKLMNOPQRST'

## =========================================================
## STONE_TO_CHAR
## ---------------------------------------------------------

STONE_TO_CHAR = {
    None: '.',
    gotypes.Player.black: 'x',
    gotypes.Player.white: 'o',
}

## =========================================================
## clear_screen()
## ---------------------------------------------------------

def clear_screen():
    """Clear the screen.
    """
    # Use `cls' on Windows;
    # and `clear' on Unix systems.
    os.system('cls' if os.name == 'nt' else 'clear')

## =========================================================
## print_move()
## ---------------------------------------------------------

def print_move(player, move, prefix='  '):

    if move.is_pass:
        move_str = 'passes'

    elif move.is_resign:
        move_str = 'resigns'

    else:
        move_str = '%s%d' % (COLS[move.point.col - 1], move.point.row)

    print('%s%s %s' % (prefix, player, move_str))

## =========================================================
## print_board()
## ---------------------------------------------------------

def print_board(board, prefix='  '):

    for row in range(board.num_rows, 0, -1):
        bump = " " if row <= 9 else ""
        line = []
        for col in range(1, board.num_cols + 1):
            stone = board.get(gotypes.Point(row=row, col=col))
            line.append(' ' + STONE_TO_CHAR[stone])
        print('%s%s%d  %s' % (prefix, bump, row, ''.join(line)))

    print('')
    print(prefix + '     ' + ' '.join(COLS[:board.num_cols]))

## =========================================================
## point_from_coords()
## ---------------------------------------------------------

def point_from_coords(coords):

    # Exit when asked for
    if coords == 'e' or coords == 'exit' or \
       coords == 'q' or coords == 'quit':
        print('')
        exit()

    # Converting the column letter to the corresponding column index
    col = COLS.index(coords[0].upper()) + 1

    # Getting the row index
    row = int(coords[1:])

    # Returning the corresponding Point
    return gotypes.Point(row=row, col=col)

## =========================================================
## =========================================================

## fin.
