row = int(input("Enter the row number: "))

col = int(input("Enter the col number: "))

print("Enter the element for matrix1: ")

matrix1 = [[int(input()) for j in range(col)] for i in range(row)]

print("matrix1:")

for i in range(row):
    
    for j in range(col):
        
        print(format(matrix1[i][j], "<3"),end = "")
    
    print()
    


print("Enter the element for matrix2: ")

matrix2 = [[int(input()) for j in range(col)] for i in range(row)]

print("matrix2:")

for i in range(row):
    
    for j in range(col):
        
        print(format(matrix2[i][j], "<3"),end = "")
    
    print()


result = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    
    for j in range(col):
        
        result[i][j] = matrix1[i][j] + matrix2[i][j]
 
print("The result is: ")

for i in range(row):
    
    for j in range(col):
        
        print(format(result[i][j], "<3"), end = "")
        
    print()
        
    
    


