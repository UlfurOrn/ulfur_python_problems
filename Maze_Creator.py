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

DIM = 3

pos_y = 0; pos_x = 0
prev_pos = []
maze = [["" for i in range(DIM)] for i in range(DIM)]
# for i in range(DIM):
#     print(maze[i])

def possible_direction():
    possible_dir = ""
    if pos_y != 0 and maze[pos_y - 1][pos_x] == "":
            possible_dir += "n"
    if pos_x != DIM - 1 and maze[pos_y][pos_x + 1] == "":
            possible_dir += "e"
    if pos_y != DIM - 1 and maze[pos_y + 1][pos_x] == "":
            possible_dir += "s"
    if pos_x != 0 and maze[pos_y][pos_x - 1] == "":
            possible_dir += "w"
    if possible_dir == "":
        possible_dir += "q"
    #print(possible_dir)
    return possible_dir

def move_dir(possible_dir):
    dir_moved = random.choice(possible_dir)
    #print(dir_moved)
    if dir_moved != "q":
        prev_pos.append(pos_x)
        prev_pos.append(pos_y)
    if dir_moved == "n":
        return pos_y - 1, pos_x, "n"
    elif dir_moved == "e":
        return pos_y, pos_x + 1, "e"
    elif dir_moved == "s":
        return pos_y + 1, pos_x, "s"
    elif dir_moved == "w":
        return pos_y, pos_x - 1, "w"
    else:
        return prev_pos.pop(), prev_pos.pop(), None


while any("" in sublist for sublist in maze):
    # prev_pos.append((pos_y, pos_x))
    pos_y, pos_x, dir_moved = move_dir(possible_direction())
    if dir_moved == "n":
        maze[pos_y][pos_x] += "s"
        maze[pos_y + 1][pos_x] += "n"
    elif dir_moved == "e":
        maze[pos_y][pos_x] += "w"
        maze[pos_y][pos_x - 1] += "e"
    elif dir_moved == "s":
        maze[pos_y][pos_x] += "n"
        maze[pos_y - 1][pos_x] += "s"
    elif dir_moved == "w":
        maze[pos_y][pos_x] += "e"
        maze[pos_y][pos_x + 1] += "w"

for i in range(DIM):
    print(maze[i])
#print(prev_pos)