from exercise_4.model import Board, Move

board = Board()
board.create_start_board(3, 3)
print(board.current_state)
possible_moves_for_V = board.get_possible_moves('V')
print(possible_moves_for_V)
print(len(possible_moves_for_V))

left_bottom_V = Move([(2, 0), (1, 0)], 'V')
right_bottom_H = Move([(2, 1), (2, 2)], 'H')

board.make_move(left_bottom_V)
print(board.current_state)
possible_moves_for_H = board.get_possible_moves('H')
print(possible_moves_for_H)
print(len(possible_moves_for_H))

board.make_move(right_bottom_H)
print(board.current_state)
possible_moves_for_V = board.get_possible_moves('V')
print(possible_moves_for_V)
print(len(possible_moves_for_V))

