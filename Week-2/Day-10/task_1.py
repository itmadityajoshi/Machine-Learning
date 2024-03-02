#Write a python progarm function to multiply all the numbers in a list

def multi(num):
    result = 1
    for i in num:
        result = i * result
        # print(result)  '''this show iteration of each value in list'''
    return result

num = [1,2,3,4,5]

print(multi(num))


