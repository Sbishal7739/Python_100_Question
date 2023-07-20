num = int(input("Enter number: "))

for row in range(num):
    for col in range(num):
        if col == 0 or row == num - 1 or row == col:
            print("*", end = "")
        else:
            print(end = " ")
    print()
    
print('-------------------------------------')
    
for row in range(num):    
    for j in range(num):
        print('*', end="")
    print()