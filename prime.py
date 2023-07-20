start = int(input("Enter the lower number: "))
end = int(input("Enter the upper number: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)