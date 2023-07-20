num = int(input("Enter the rows: "))

for i in range(num, 0, -1):
    
    for j in range(i, 0, -1):
        
        print("*", end = "")
        
    for j in range(2*(num - i)):
        
        print(" ", end = "")
        
    for j in range(i, 0, -1):
        
        print("*", end = "")
                       
    print()
    
for i in range(num):
    
    for j in range(i):
        
        print("*", end = "")
        
    for j in range(2*(num - i)):
        
        print(" ", end = "")
        
    for j in range(i):
        
        print("*", end = "")
                       
    print()