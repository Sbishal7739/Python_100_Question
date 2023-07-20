
qs1 = """1) What is the maximum possible length of an identifier?

    a.16
    b.32
    c.64
    d.None of these above
"""
 
qs2 = """2) Who developed the Python language?

    a.Zim Den
    b.Guido van Rossum
    c.Niene Stom
    d.Wick van Rossum
    """

qs3 = """ 3)In which year was the Python language developed?

    a.1995
    b.1972
    c.1981
    d.1989
"""

qs4 = """5) Which one of the following is the correct extension of the Python file?

    a. .py
    b. .python
    c. .p
    d. None of these
"""

question = {qs1:"d", qs2:"b", qs3:"d", qs4:"a"}

name = input("Enter your name: ")

print("Hello", name , "enter the quiz world")

score = 0

for i in question:
    
    print(i)
    
    skip = input("Do you want to skip this question enter y/n: ")
    
    if skip == "yes":
        
        continue
    
    ans = input("Enter the answer (a/b/c/d): ")
    
    if ans == question[i]:
        
        print("The answer is correct, you got 1 point")
        
        score = score + 1
        
    else:
        
        print("The answer is incorrect, you lost 1 point")
        
        score = score - 1
        
    quitt = input("Do you want to quit (y/n)")
    
    if quitt == "yes":
        
        break
        
print("The final score is: ",score)
    
    