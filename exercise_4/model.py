import numpy as np


class Move:
    coordinates: list[tuple]
    player: str

    def __init__(self, coordinates, player):
        self.coordinates = coordinates
        self.player = player

    def __repr__(self):
        return f"{self.coordinates, self.player}"


class Board:
    current_state: np.ndarray

    def get_possible_moves(self, player: str) -> list[Move]:
        possible_moves: list[Move] = []
        for i in range(len(self.current_state)):
            for j in range(len(self.current_state[i])):
                if self.current_state[i][j] == 0:
                    if player == 'V':
                        if (
                                i + 1 < len(self.current_state)  # check if end (bottom) of matrix reached
                                and self.current_state[i + 1][j] == 0
                        ):
                            possible_moves.append(Move([(i, j), (i + 1, j)], 'V'))
                    elif player == 'H':
                        if (
                                j + 1 < len(self.current_state) # check if end (right end) of matrix reached
                                and self.current_state[i][j + 1] == 0
                        ):
                            possible_moves.append(Move([(i, j), (i, j + 1)], 'H'))

        return possible_moves

    def make_move(self, move: Move):
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
