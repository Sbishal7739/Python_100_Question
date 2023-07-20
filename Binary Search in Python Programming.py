def bainary_search(list1, k):
    
    
    start = 0

    end = len(list1) - 1

    mid = (start + end) // 2

    found = False

    while(start <= end) and not found:
    
        if list1[mid] == k:
        
            found = True
        
        elif (k > list1[mid]):
        
            start = mid + 1
        
        else:
            end = mid - 1
            
        mid = (start + end) // 2
            
    if found == True:
        print("Key is found")
    
    else:
        print("Key is not found")
    
def short_array(num):
    
    for i in range(len(num) - 1):
    
        min_value = min(num[i:])
    
        min_index = num.index(min_value, i)
    
        num[i], num[min_index] = num[min_index], num[i]

    #print(num)
    return num


num = [10,1,4,7,3,8,41,50]

key = 51

list1 = short_array(num)

bainary_search(list1, key)






    
    
    
    