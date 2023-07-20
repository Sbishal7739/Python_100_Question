st = input("Enter your name: ")
for row in range(len(st)):
    for col in range(row + 1):
        print(st[col], end = "")
    print()