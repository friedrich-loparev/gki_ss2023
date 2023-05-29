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

    def get_possible_moves(self, player: str) -> list[Move]:

        if player == 'V':
            pass
        elif player == 'H':
            pass
        else:
            raise KeyError('Illegal player.')

    def make_move(self, move: Move):
        """Takes next move as input and performs the move."""
        if move.player == 'V':
            for position in move.coordinates:
                self.current_state[position] = 1
        elif move.player == 'H':
            for position in move.coordinates:
                self.current_state[position] = 2
        else:
            raise KeyError('Illegal player.')

    def create_start_board(self, rows: int, columns: int) -> None:
        self.current_state = np.zeros((rows, columns), dtype=np.int32)


def game_over(board: Board) -> bool:
    pass


def evaluate(board: Board):
    """A function that evaluates the current state of the board and returns a score."""
    pass
