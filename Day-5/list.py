# PYTHON LIST

# list1 = ["name",1,3,5,"apple",True]
# print(list1)

#display Type
# print(type(list1))

# display length of list
# print(len(list1))

# Nested List

# Nest_list = [["a","b"],[1,2]]
# print(Nest_list)

# length of Nested List

# print(len(Nest_list))


# List creation from Strings

# name = "Ram Gurung"
# print(name.split())

# Indexing in Lists

# fruits = "apple banana pear grapes mango"

# lis_fruit = fruits.split()  #this will make list with items of frutis of strings
# print(lis_fruit)


# print(lis_fruit[0])  #apple

# print(lis_fruit[2])

# print(lis_fruit[4])

# print(lis_fruit[-5])
# print(lis_fruit[-3])
# print(lis_fruit[-1])



# Now Lets try to index nested list

# mix = [[1,2],["a","b"],["fname","lname"],[True,False],["CSIT","BCA"]]
# print(mix[0])
# print(mix[2])
# print(len(mix))



#Loops using enumerate

# fruits = ['mango','banana','kiwi','apple','grapes']

# # using enumerate() method
# print(list(enumerate(fruits)))

# print(list(enumerate(fruits,2)))  #here 2 is the counting value form where the iteration starts
    

# List comprehension 

# fruits = ["aPPLE","MaNGO","BANaNA","GRaPes", "coffe"]
# newlist = [ for x in fruits]

# print(newlist)




# Q.1.


fruits = ["aPPLE","MaNGO","BANaNA","GRaPes", "coffe"]

longest = max(fruits, key=len)
print(longest)


# Q.2.

sample_list = [1,2,3,4,5]
sum= 0
for x in sample_list:
    sum += x
print(sum)


# Q.3.

num_list = [10,20,30,100,40]

b = max(num_list)
print(b)


# Q.4.

num_list1=[-1,0,1,2]

s = min(num_list1)
print(s)

# Q.5.

var1 = ['aba','xyz','aba','1221']

print(var1.count('aba'))

