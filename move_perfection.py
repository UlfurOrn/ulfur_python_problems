Min_constant = 1
Max_constant = 10

def select_index():
    starting_index = input("Input a position between {} and {}: ".format(Min_constant, Max_constant))
    if starting_index.isdigit() and Min_constant <= int(starting_index) <= Max_constant:
        return int(starting_index)
    else:
        print("Invalid input, try another \n ")
        return select_index()

def create_map(index):
    position = (Max_constant - Min_constant + 1) * "x"
    position = position[:index - 1] + "o" + position[index:]
    print(position)

def move_right(index):
    if index == Max_constant:
        return index
    else:
        return index + 1

def move_left(index):
    if index == Min_constant:
        return index
    else:
        return index - 1

def select_move(player_input, index):
    if player_input == "r":
        return move_right(index), True

    elif player_input == "l":
        return move_left(index), True

    else: 
        return index, False

def start_game():
    play_game = True
    index = select_index()
    create_map(index)
    
    print("l - for moving left \nr - for moving right \nAny other letter for quitting")

    while play_game:
        index, play_game = select_move(input("Input your choice: "), index)
        create_map(index)

start_game()