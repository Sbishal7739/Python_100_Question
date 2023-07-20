
list2 = []

def get_max(list1):
    
    for i in list1:
        
        if type(i) == list:
            
            get_max(i)
            
        else:
            
            list2.append(i)
            
    return max(list2)


list1 = [5,10,[20,4],6,[4,[8,2]]]

print(get_max(list1))