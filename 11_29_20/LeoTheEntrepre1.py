def isPrime(num):
    from math import sqrt
    return num >=2 and not [n for n in range(2, int(sqrt(num))) if num % n == 0]
