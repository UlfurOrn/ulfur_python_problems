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

import random

pos_y = 0; pos_x = 0
prev_pos = []
maze = [[0 for i in range(5)] for i in range(5)]
maze[pos_y][pos_x] = 1
for i in range(5):
    print(maze[i])

def possible_direction():
    possible_dir = ""
    if pos_y != 0 and maze[pos_y - 1][pos_x] == 0:
            possible_dir += "n"
    if pos_x != 4 and maze[pos_y][pos_x + 1] == 0:
            possible_dir += "e"
    if pos_y != 4 and maze[pos_y + 1][pos_x] == 0:
            possible_dir += "s"
    if pos_x != 0 and maze[pos_y][pos_x - 1] == 0:
            possible_dir += "w"
    if possible_dir == "":
        possible_dir += "q"

    print(possible_dir)
    return possible_dir

def move_dir(possible_dir):
    dir_moved = random.choice(possible_dir)
    print(dir_moved)
    if dir_moved != "q":
        prev_pos.append((pos_y, pos_x))
    if dir_moved == "n":
        return pos_y - 1, pos_x
    elif dir_moved == "e":
        return pos_y, pos_x + 1
    elif dir_moved == "s":
        return pos_y + 1, pos_x
    elif dir_moved == "w":
        return pos_y, pos_x - 1
    else:
        return prev_pos.pop()


while any(0 in sublist for sublist in maze):
    # prev_pos.append((pos_y, pos_x))
    pos_y, pos_x = move_dir(possible_direction())
    maze[pos_y][pos_x] = 1


    for i in range(5):
        print(maze[i])
print(prev_pos)