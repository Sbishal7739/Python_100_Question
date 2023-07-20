sentances = input("Enter the sentances: ")

string = sentances.lower()

count = 0

list = ["a","e","i","o","u"]

for char in string:
    
    if char in list:
        
        count = count + 1
        
print("No of vowel given sentanves is:",count)