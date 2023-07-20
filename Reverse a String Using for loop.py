def reverce_string(string):
    r_string = ""
    for i in string:
        r_string = i + r_string
    print("Reverce string is ",r_string)
    
    
string = input("Enter your string: ")
reverce_string(string)