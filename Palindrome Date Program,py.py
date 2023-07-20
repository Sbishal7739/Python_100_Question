date = input("Enter the date in dd/mm/yyyy format: ")

given_date = date.replace('/',"")

rev_date = given_date[::-1]

if given_date == rev_date:
    
    print("The date is palindrom")
    
else:
    
    print("The date is not palindrom")