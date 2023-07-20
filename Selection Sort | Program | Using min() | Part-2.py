list = [3,2,5,7,2]

for i in range(len(list)-1):
    min_value = min(list[i:])
    min_index = list.index(min_value,i)
    list[i], list[min_index] = list[min_index], list[i]
    print(list)