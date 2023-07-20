list = []

num = int(input("how many numbers you want to enter: "))

for k in range(num):
    list.append(int(input("Enter values: ")))

print("Unsorted list: ",list)

for i in range(len(list) - 1):
    
    for j in range(len(list) - 1 - i):
        
        if list[j] > list[j + 1]:
            
            # Swap
            list[j], list[j+1] = list[j+1], list[j]
            
            print(list)
        else:
            print(list)
    print()
            
print("Sorted list: ",list)