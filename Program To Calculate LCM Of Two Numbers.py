def lcm(n1, n2):
    
    
    if n1 > n2:
        
        higher = n1
        
    else:
        
        higher = n2
        
    while True:
        
        value = higher
        
        if higher % n1 == 0 and higher % n2 == 0:
            
            print("lcm of", n1, "and", n2, "is", higher)
            
            break
            
        else:
            
            higher = higher + value
        
        
num1 = int(input("Enter your first number: "))

num2 = int(input("Enter tour second number: "))

lcm(num1, num2)