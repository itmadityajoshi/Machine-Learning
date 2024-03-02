'''Q.7 Write a Python function that takes a number as a parameter and check the
number is prime or not'''

def check_prime(n):
    if n == 1:
        print('Number is not a prime number.')
    elif n > 1:
        for i in range(2):
            if (n % 2) == 0:
                print(n,'is not a prime number.')
                break
            else:
                print(n,'is a prime number.')
    else:
        print(n,'is not a prime number.')


check_prime(9)

