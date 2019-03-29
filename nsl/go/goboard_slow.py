## =========================================================
## nsl/go/goboard_slow.py
## ---------------------------------------------------------

import copy
from nsl.go.gotypes import Player

## =========================================================
## class GoString
## ---------------------------------------------------------

class GoString():
    """Go strings are stones that are linked by a chain of connected
    stones of the same color.

    """
    def __init__(self, color, stones, liberties):
        self.color = color
        self.stones = set(stones)
        self.liberties = set(liberties)

    def remove_liberty(self, point):
        self.liberties.remove(point)

    def add_liberty(self, point):
        self.liberties.add(point)

    def merged_with(self, go_string):  # <2>
        """Return a new Go string containing all stones in both strings.

        """
        assert go_string.color == self.color
        combined_stones = self.stones | go_string.stones
        return GoString(
            self.color,
            combined_stones,
            (self.liberties | go_string.liberties) - combined_stones)

    @property
    def num_liberties(self):
        return len(self.liberties)

    def __eq__(self, other):
        return isinstance(other, GoString) and \
            self.color == other.color and \
            self.stones == other.stones and \
            self.liberties == other.liberties

## =========================================================
## class Board
## ---------------------------------------------------------

class Board():
    """A board is initialized as empty grid with the specified number of
    rows and columns.

    """
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}

## =========================================================
## class Move
## ---------------------------------------------------------

class Move():
    """
    Any action a player can play on a turn, 
    either is_play, is_pass or is_resign will be set.
    """
    def __init__(self, point=None, is_pass=False, is_resign=False):
        assert (point is not None) ^ is_pass ^ is_resign
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign

    @classmethod
    def play(cls, point):
        """
        This move places a stone on the board.
        """
        return Move(point=point)

    @classmethod
    def pass_turn(cls):
        """
        This move passes.
        """
        return Move(is_pass=True)

    @classmethod
    def resign(cls):
        """
        This move resigns the current game
        """
        return Move(is_resign=True)

## =========================================================
## =========================================================

## fin.
