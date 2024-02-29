'''Create a program that generates a word pyramid pattern based on user input'''


str = input("Enter the string as you want : ")
word = len(str)
for i in range(0, word):
    for j in range(0, word-0-i):
        print(end=" ")
    for j in range(0,i+1):
        print(str[j], end=" ")
    print() 
print()
    
# to print downward:
    
for i in range(word,0,-1):
    for j in range(0, word-i):
        print(end=" ")
    for j in range(0,i):
        print(str[j], end=" ")
    print()
    
