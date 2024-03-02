'''Q.8 Write a python function to print the even numbers from a given list'''

def even_num(num):
    a = []
    for i in num:
        if i % 2 == 0:
            a.append(i)
        else:
            pass
    return a


num = [1,2,3,4,5,6,7,8,9,12,10,60,55]
print(even_num(num))