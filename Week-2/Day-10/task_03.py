'''Q.3 Write a python function to find factorial of a given non negativenumber'''

def factorial(num):
    if (num==0 or num==1):
        return 1
    
    else:
        return num * factorial(num-1)


print(factorial(5))
print(factorial(1))
print(factorial(7))
print(factorial(2))


