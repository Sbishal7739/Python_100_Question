# import math
# print(math.gcd(108,109))


def compute_gcd(a, b):
    if b == 0:
        return a
    else:
        return compute_gcd(b, a%b)
    
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(compute_gcd(num1, num2))
