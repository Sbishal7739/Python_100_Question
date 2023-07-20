import math

def perfect_sqrt(n):
    
    res = int(math.sqrt(n))
    
    return res * res == n

num = int(input("Enter your number: "))

result1 = 5 * (num * num) + 4

result2 = 5 * (num * num) - 4

if perfect_sqrt(result1) or perfect_sqrt(result2):
    
    print(num, "This number is a fibonacci number")
    
else:
    
    print(num,"This number is not a fibonacci number")
