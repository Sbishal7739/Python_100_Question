name1 = input("Enter your 1st name: ").lower()

name2 = input("Enter your 2nd name: ").lower()

name1 = name1.replace(" ","")

name2 = name2.replace(" ","")

for i in name1:
    
    for j in name2:
        
        if i == j:
            
            name1 = name1.replace(i,"",1)
            
            name2 = name2.replace(j,"",1)
            
            break
            
print(name1)

print(name2)

count = len(name1 + name2)

print(count)

if count > 0:
    
    list1 =["Friends","Lovers","Affectionate","Marriage","Enemies","Siblings"]
    
    while len(list1) > 1:
        
        c = count % len(list1)
        
        set_index = c - 1
        
        if set_index > 0:
            
            left = list1[:set_index]
            
            right = list1[set_index + 1:]
            
            list1 = right + left
            
            #print(list1)
            
        else:
            
            list1 = list1[:len(list1) - 1]
            
    print("The relationship is:",list1[0])
    
else:
    
    print("Enter diffarent name")