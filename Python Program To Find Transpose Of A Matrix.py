p = int(input("Enter the row number: "))

q = int(input("Enter the column number: "))

print("Enter the elements for matrix 1:")

matrix1 = [[int(input()) for j in range(q)] for i in range(p)]

print("Matrix 1:")

for i in range(p):
    
    for j in range(q):
        
        print(format(matrix1[i][j], "<3"), end="")
        
    print()
 
 
 
result = [[0 for i in range(p)] for i in range(q)]

for i in range(q):
    
    for j in range(p):
        
        result[i][j] = matrix1[j][i]
        
print("The transpose matrix is:")
        
for i in range(q):
    
    for j in range(p):
        
        print(format(result[i][j], "<3"),end = "")
        
    print()


    