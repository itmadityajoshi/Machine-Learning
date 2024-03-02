'''Write a python function that takes a list and returns a new list with unique elements of the first list'''


def unique(nums):
    new_list = []

    for i in nums:
        if i not in new_list:
            new_list.append(i)

    return new_list



print(unique([1,2,2,3,3,3,4,4,5,5,6,7,8,8,9,0,2,]))