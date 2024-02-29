# Prime Factorization 

def prime_factors(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1

    return factors

number = int(input("Enter a number: "))

print("prime factors of ", number,"are:", prime_factors(number))

