num = int(input("Enter your number: "))

n = 1
for row in range(1,num):
    for col in range(1,row+1):
        print(n, end = " ")
        n += 1
    print()
        
    