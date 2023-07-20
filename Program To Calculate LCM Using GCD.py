def compute_gcd(n1,n2):
    
    if n2 == 0:
        
        return n1
    
    else:
        
        return(compute_gcd(n2, n2 % n1))

        
num1 = int(input("Enter your first number: "))

num2 = int(input("Enter tour second number: "))

lcm = (num1 * num2) // compute_gcd(num1, num2)

print(lcm)


