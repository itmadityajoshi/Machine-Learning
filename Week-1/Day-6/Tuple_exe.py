# .1 Write a python program to lowercase item in given Tuples using Tuple comprehension.

sample_tuple = ("APPLE", "Mango", "BaNaNa", "GRapes")

lower_tuple = tuple(item.lower() for item in sample_tuple)

print(lower_tuple)



# using enumerate() function to loop Tuples

simple_tuple1 = ("item1",2,"item3",4)

for x, item in enumerate(simple_tuple1):
    print(x, item)
    print('----------')


# unpack Tuples using *asterik
    a, *b, c = sample_tuple = ("item1", 2,3,"item4",5)
    print(b)


# addition of tuples

simple_tuple = ('item1',2,'item3',6)

list_from_tuple = list(simple_tuple)
list_from_tuple.append("item5")
simple_tuple = tuple(list_from_tuple)

print(simple_tuple)


