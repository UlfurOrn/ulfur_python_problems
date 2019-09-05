for num in range(1,100):
    num_div = 0
    for div in range(1, num + 1):
        if num % div == 0:
            num_div += 1
    if num_div == 10:
        print(num)
print("Hello")