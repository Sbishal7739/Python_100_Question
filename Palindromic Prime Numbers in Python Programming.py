num = int(input("Enter your number: "))

result = 0

rev_num = int(str(num)[::-1])

for i in range(2, num):
    
    if num % i == 0:
        
        print("Not prime")
        
        break
    
else:
    
    if num == rev_num:
        
        print(num, "The number is palindromic prime number")
    
    else:
        
        print(num, "The number is only prime number")