def convert_notation_to_coordinates(position):
    column = ord(position[0]) - ord('a') + 1
    row = int(position[1])
    return (row, column)

board = [[0 for i in range(8)] for j in range(8)]
initial_position = input()
final_position = input()
initial_position = convert_notation_to_coordinates(initial_position)
final_position = convert_notation_to_coordinates(final_position)
