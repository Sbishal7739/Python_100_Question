num = int(input("Enter your number: "))

for row in range(num):
    for col in range(num):
        if row == 0 or col== num - 1 or row == col:
            print('*', end = "")
        else:
            print(end = " ")
    print()
   
   
   