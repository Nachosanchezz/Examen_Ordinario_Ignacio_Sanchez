def convert_notation_to_coordinates(position):
    column = ord(position[0]) - ord('a') + 1
    row = int(position[1])
    return (row, column)

board = [[0 for i in range(8)] for j in range(8)]
initial_position = convert_notation_to_coordinates("a3")
final_position = convert_notation_to_coordinates("b5")
board[initial_position[0]][initial_position[1]] = 0
board[final_position[0]][final_position[1]] = 1


from collections import deque

def is_valid_move(position, board):
    return 0 <= position[0] < 8 and 0 <= position[1] < 8 and board[position[0]][position[1]] == -1


def bfs(initial_position, final_position, board):
    queue = deque()
    queue.append((initial_position, 0))
    board[initial_position[0]][initial_position[1]] = 0
    while queue:
        current_position, distance = queue.popleft()
        if current_position == final_position:
            return distance
        for move in [(1, 2), (2, 1), (1, -2), (-2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1)]:
            next_position = (current_position[0] + move[0], current_position[1] + move[1])
            if is_valid_move(next_position, board):
                queue.append((next_position, distance + 1))
                board[next_position[0]][next_position[1]] = distance + 1
    return -1
result = bfs(initial_position, final_position, board)
print(result)
   
