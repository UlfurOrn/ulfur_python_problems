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

if 1 in maze:
    print(True)
maze[pos_y][pos_x] = 1
if 1 in maze:
    print(True)

for i in range(5):
    print(maze[i])