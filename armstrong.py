for i in range(1,1000):
    num = i
    result = 0
    n = len(str(i))
    while(i != 0):
        mod = i % 10
        result = result + mod ** n
        i = i // 10
    if num == result:
        print(result)
