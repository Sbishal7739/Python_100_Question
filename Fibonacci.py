num = int(input("Enter a number: "))

first = 0
second = 1
for i in range(num):
    print(first)
    
    temp = first
    first = second
    second = temp + first