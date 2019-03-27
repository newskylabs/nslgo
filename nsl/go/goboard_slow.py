## =========================================================
## nsl/go/goboard_slow.py
## ---------------------------------------------------------

import copy
from nsl.go.gotypes import Player

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
