num = int(input("Enter the number: "))


for i in range(1, num + 1):
    result = 0
    for j in range(1, i):
        if i % j == 0:
            result = result + j
    if result == i:
        print(i, "is a perfect number")
    else:
        print(i, "is not a perfect number")
            