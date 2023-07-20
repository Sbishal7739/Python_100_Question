# for row in range(1,5):
#     for col in range(1,8):
#         if row == 4 or row + col == 5 or col - row == 3:
#             print('*', end="")
#         else:
#             print(end = " ")
#     print()



num = int(input("Enter the number of rows"))

for row in range(1, num + 1):
    for col in range(1, num * 2):
        if row == num or row + col == num + 1 or col - row == num - 1:
            print('*', end="")
        else:
            print(end=" ")
    print()