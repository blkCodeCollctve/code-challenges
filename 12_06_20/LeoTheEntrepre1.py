def maxMultiple(divisor, bound):
    return max([n for n in range(bound, 0, -1) if n % divisor == 0])
