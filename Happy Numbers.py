def sumofdigits(n):
    
    summ = 0
    
    rem = 0
    
    while n > 0 :
        
        rem = n % 10
        
        summ = summ + rem * rem
        
        n = n // 10
        
    return summ


num = int(input("Enter the number: "))

result = num

while result != 1 and result != 4:
    
    result = sumofdigits(result)
    
    
if result == 1:
    
    print(num, "is a happy number")
    
else:
    
    print(num, "is not a happy number")
