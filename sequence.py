n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_num = 1
second_num = 2
third_num = 3

for i in range(1, n+1):
    if i <= 3:
        print(i)
    else:
        new_num = first_num + second_num + third_num
        first_num, second_num, third_num = second_num, third_num, new_num
        print(new_num)