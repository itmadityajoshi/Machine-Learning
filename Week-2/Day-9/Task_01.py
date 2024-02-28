'''Create a program that generates a word pyramid pattern based on user input'''


# str = input("Enter the string as you want : ")

# for i in range(len(str)):
#     for j in range(len(str)-i):
#         print(str, end="")
    


rows = 5
for i in range(rows+1):
    for j in range(i):
        print(i, end="")
    print()