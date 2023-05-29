from exercise_4.model import Board, Move
import numpy as np

board = Board()
board.create_start_board(3, 3)
print(board.current_state)

left_bottom_V = Move([(2, 0), (1, 0)], 'V')
right_bottom_H = Move([(2, 1), (2, 2)], 'H')

board.make_move(left_bottom_V)
print(board.current_state)

board.make_move(right_bottom_H)
print(board.current_state)

# Iterate over board --> Use in get_possible_moves
for i in np.nditer(board.current_state):
    print(f"i = {i}")
