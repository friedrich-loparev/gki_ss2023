import sys

import numpy as np


class Move:
    coordinates: list[tuple]
    player: str

    def __init__(self, coordinates, player):
        self.coordinates = coordinates
        self.player = player


class Board:
    """Represents state of the board"""

    current_state: np.ndarray

    def make_move(self, move: Move):
        """Takes next move as input and performs the move."""
        try:
            if move.player == 'V':
                for position in move.coordinates:
                    self.current_state[position] = 2
            elif move.player == 'H':
                for position in move.coordinates:
                    self.current_state[position] = 1
        except KeyError:
            sys.exit(1)

    def create_start_board(self, rows: int, columns: int) -> None:
        self.current_state = np.zeros((rows, columns), dtype=np.int32)


def game_over(board: Board) -> bool:
    pass


def evaluate(board: Board):
    """A function that evaluates the current state of the board and returns a score."""
    pass


def get_possible_moves(board: Board):
    """A function that returns a list of all possible moves from the current state."""
    pass
