nums = int(input("Enter the number of rows: "))

for i in range(nums):
    
    k = 111
    
    for j in range(i):
        
        print(format(k, "<4"),end = "")
        
        k = k + 111
        
    print()