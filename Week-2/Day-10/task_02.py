# Q.2 Write a python function to reverse a string


def ulto(word):
    sabda = word[::-1]
    return sabda

word = input('enter the string : ')
print(ulto(word))