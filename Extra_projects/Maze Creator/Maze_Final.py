import random

DIM = 20

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

import turtle

len_box = int(600 / DIM)

turtle.hideturtle()
turtle.penup()
turtle.speed(0)
turtle.setx(-300)
turtle.sety(300)
turtle.pendown()

for i in range(4):
    turtle.forward(len_box * DIM)
    turtle.right(90)

turtle.forward(len_box)
turtle.right(90)

for i in range(DIM):
    for j in range(DIM):
        if "e" in maze[j][i]:
           turtle.penup() 
        turtle.forward(len_box)
        turtle.pendown()
    turtle.penup()
    turtle.backward(len_box * DIM)
    turtle.left(90)
    turtle.forward(len_box)
    turtle.right(90)
    turtle.pendown()

turtle.penup()
turtle.setx(-300)
turtle.sety(300 - len_box)
turtle.left(90)
turtle.pendown()

for i in maze:
    for j in i:
        if "s" in j:
           turtle.penup() 
        turtle.forward(len_box)
        turtle.pendown()
    turtle.penup()
    turtle.backward(len_box * DIM)
    turtle.right(90)
    turtle.forward(len_box)
    turtle.left(90)
    turtle.pendown()


turtle.penup()
turtle.setx(-300 + DIM * (len_box) - len_box / 2)
turtle.sety(300 - DIM * (len_box) + len_box / 2)
turtle.pensize(len_box / 2)
turtle.pencolor("orange")
turtle.pendown()
turtle.forward(0)

turtle.penup()
turtle.setx(-300 + len_box / 2)
turtle.sety(300 - len_box / 2)
turtle.pensize(len_box / 2)
turtle.pencolor("lightgreen")
turtle.pendown()
turtle.forward(0)

def pick_dir(available_dir):
    player_select = input("Direction: ").lower()
    if player_select == "":
        player_select = "q"
    if player_select in available_dir:
        if player_select == "w":
            turtle.pencolor("white")
            turtle.pendown()
            turtle.forward(0)
            turtle.penup()   
            return pos_y - 1, pos_x
        elif player_select == "d":
            turtle.pencolor("white")
            turtle.pendown()
            turtle.forward(0)  
            turtle.penup() 
            return pos_y, pos_x + 1
        elif player_select == "s":
            turtle.pencolor("white")
            turtle.pendown()
            turtle.forward(0) 
            turtle.penup()  
            return pos_y + 1, pos_x
        elif player_select == "a":
            turtle.pencolor("white")
            turtle.pendown()
            turtle.forward(0)  
            turtle.penup() 
            return pos_y, pos_x - 1
    else:
        return pick_dir(available_dir)

def print_dir(available_dir):
    print("You can travel:", end=" ")
    for c in available_dir:
        if c == "n":
            print("(N)orth", end=" ")
        elif c == "e":
            print("(E)ast", end=" ")
        elif c == "s":
            print("(S)outh", end=" ")
        elif c == "w":
            print("(W)est", end=" ")
        if c != available_dir[-1]:
            print("or", end=" ")
    print("")

def nesw_to_wasd(directions):
    new_dir = ""
    if "n" in directions:
        new_dir += "w"
    if "e" in directions:
        new_dir += "d"
    if "s" in directions:
        new_dir += "s"
    if "w" in directions:
        new_dir += "a"
    return new_dir
    

pos_y = 0; pos_x = 0

while True:
    print_dir(maze[pos_y][pos_x])
    pos_y, pos_x = pick_dir(nesw_to_wasd(maze[pos_y][pos_x]))
    turtle.setx(-300 + len_box / 2 + len_box * pos_x)
    turtle.sety(300 - len_box / 2 - len_box * pos_y)
    turtle.pencolor("lightgreen")
    turtle.pendown()
    turtle.forward(0)
    turtle.penup()
    if pos_y == DIM - 1 and pos_x == DIM - 1:
        print("Victory!")
        break

turtle.mainloop()