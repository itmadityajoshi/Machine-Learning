''' create a program that analyzes a given text and 
counts the frequency of each unique word '''


def count(user_input):
    word = (user_input.split())
    print(word)
    word2 = [] #initalize empty list

    #loop till string values present in list word2
    for i in word:

        # checking for hte duplicate
        if i not in word2:

            word2.append(i) #insert word in word2 
    
    for i in range(0, len(word2)):

        # count the frequency of each word present in word2
        print('Frequency of ', word2[i], 'is :', word.count(word2[i]))


user_input = input("Enter the string for word count.")
count(user_input)
