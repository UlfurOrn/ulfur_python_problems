"""
Create grid
    while
        1. From any given point in grid find random empty neighbor
        2. remove wall
        3. add current position to list
        4. move to new position
    else
        1. If no empty neighbor move to position latest in stack
        2. Remove old position from stack
"""

pos_x = 0; pos_y = 0
maze = [[0 for i in range(5)] for i in range(5)]
maze[pos_y][pos_x] = 1
maze[-1][0] = 1
for i in range(5):
    print(maze[i])

def possible_direction():
    count_dir = 0
    if pos_y != 4 and maze[pos_y + 1][pos_x] == 0:
            count_dir += 1
    if pos_y != 0 and maze[pos_y - 1][pos_x] == 0:
            count_dir += 1
    if pos_x != 4 and maze[pos_y][pos_x + 1] == 0:
            count_dir += 1
    if pos_x != 0 and maze[pos_y][pos_x - 1] == 0:
            count_dir += 1
    print(count_dir)

possible_direction()