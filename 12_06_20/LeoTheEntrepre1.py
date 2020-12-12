def maxMultiple(divisor, bound):
    return max([n for n in range(bound+1) if n % divisor == 0])
