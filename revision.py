num = 1
while num <= 20:
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is a multiple of 3 and 5")
    elif num % 3 == 0:
        print(f"{num} is a multiple of 3")
    elif num % 5 == 0:
        print(f"{num} is a multiple of 5")
    num += 1