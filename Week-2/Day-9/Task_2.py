'''LIST Manipulation  Odd-Even sorter'''

def check(numbers):
    Odd_num = []
    Even_num = []
    for i in numbers:
        if i % 2 == 0:
            Even_num.append(i)
        else:
            Odd_num.append(i)
    
    print(f'odd numbers : {Odd_num}')
    print(f'even numbers : {Even_num}')


numbers = int(input('ente the numbers. \n'))
A =[]
for i in range(int(numbers)):
    k = int(input(""))
    A.append(k)

check(numbers)


