str1 = input("Enter the string: ")

print("1. upper 2. lower 3. swap 4. title")

n = int(input("Select the operation: "))

if n == 1:
    
    print(str1.upper())
    
elif n == 2:
    
    print(str1.lower())
    
elif n == 3:
    
    print(str1.swapcase())
    
elif n == 4:
    
    print(str1.title())
    
else:
    
    print("Enter the correct operation")