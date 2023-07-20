# Selection Sort
list = [10,13,84,45,3,30]

print(list)

for i in range(len(list)):
    min_value = min(list[i:])
    min_index = list.index(min_value)
    list[i], list[min_index] = list[min_index], list[i]
print(list)