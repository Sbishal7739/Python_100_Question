num = int(input("Enter your number: "))

k = (num * 2) - 1

matrix = [[j for j in range(k)] for i in range(k)]

for i in range(k):
    
    for j in range(k):
        
        print(matrix[i][j], end = "")
        
    print()