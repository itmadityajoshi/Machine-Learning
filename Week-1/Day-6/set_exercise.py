set1 = {'item1', True, False}


print(set(set1))

# display datatype

print(type(set1))


# create simple set with mixed data types

mixset = {'apple',2,'shoes','b','mango',0, True}
print(type(mixset))

# length of set

print(len(mixset))


# Sets Methods/Operations

set_methods = {'scale',0,'set','methods', True, 1}
print(set_methods)

# add () method in Sets

set_methods.add('orange')
set_methods.add('Mock')
set_methods.add('Test')


print(set_methods)


# remove () in sets

set_methods.remove('Test')
print(set_methods)

# pop () in sets

set_methods.pop()  #generally pop method is to remove an item, but this method wull remove a random item.
# generally, it remove from starting item in a set.
print(set_methods) 


# uinion() methods in Sets

setA = {1,2,3,5,6,'a','s','d','e','f'}
setB = {'a','b','c','d','e','f',2,4,5,6}

print(setA)
print(setB)

union_set = setA.union(setB)
print(f"Union of setA and setB is:{union_set}")

# union of set using (|) operator

slash_operator = setA | setB
print(f"union using slash operator: {slash_operator}")

# intersection() in sets

set_intersection = setA and setB
print(set_intersection)


# difference () in sets

diff_sets = setA - setB
print(diff_sets)

# loop

for x in setA:
    print(x)


# set Comprehension
    
set_comprehension = ['item',1,2,'item4']

set_list = set(set_comprehension)
print(set_list)

for x in set_list:
    print(x)


set(item for item in set_list)
print(set)


# sorting

number = {1,2,4,5,8,0,6,9,10}
print(sorted(number))