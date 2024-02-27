'''Create a program that checks if a given string can be 
rearranged to form a palindromic string'''

def check(user_input):

    word_1 = user_input.lower()
    print(word_1)
    word_2 = word_1[::-1]
    print(word_2)

    if word_1 == word_2:
        print("The word is Plaindrome")
    else:
        print("The word is not Palindrome")



user_input = input("Enter to check palindrome. ")

check(user_input)