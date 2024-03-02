'''Q.5 Write a python function that accepts a string and calculate the number of upper case letters and lower case letters'''



def calcStr(sabda):
    lower_count = 0
    upper_count = 0

    for char in sabda:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count +=1 
    
    return upper_count, lower_count



sabda = input('Enter the string as you wish : ')
upper, lower = calcStr(sabda)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
