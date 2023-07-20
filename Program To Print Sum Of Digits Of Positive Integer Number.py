num = int(input("Enter your number: "))

size = len(str(num))

result = 0

if num > 0:
    for i in range(size):
    
        result = result + (num % 10)
    
        num = int(num / 10)
    print(result)

else:
    print("Enter positive number")
    



