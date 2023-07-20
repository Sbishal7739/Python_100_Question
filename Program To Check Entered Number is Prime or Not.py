num = int(input("Enter any positive numbern to check the number is positive or not: "))

if num > 1:
    for i in range(2, num ):
        if num % i == 0:
            print(num, "is not a  prime number")
            break
    else:
        print(num, "is a Prime number")
