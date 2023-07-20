day = int(input("Enter the day(dd)"))

month = int(input("Enter the month(mm)"))

year = int(input("Enter the year(yyyy)"))


if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    
    max_days = 31
    
elif month == 4 or month == 6 or month == 9 or month == 12:
    
    max_days = 30
    
elif year % 400 == 0 or ( year % 400 == 0 and year % 100 != 100):
    
    max_days = 29
    
else:
    
    max_days = 28
    
    
if day < 1 or day > max_days:
    
    Print("Invalid days")
    print("Plece check range of days")
    
elif month <1 or month > 13:
    
    print("Invalid month")
    print("Plece check range of month")
    
else:
    print("The date is valid")