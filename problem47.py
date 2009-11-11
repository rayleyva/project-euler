import math

def is_prime(n):
    if n < 2:
        return False
    for j in range(2, math.sqrt(n) + 1):
        if n%j == 0:
            return False
    return True

def get_factors(n):
    factors = []
    for j in range(2, math.sqrt(n) + 1):
        if n%j == 0:
            factors.append(j)
            factors.append(n/j)
    return factors

def get_prime_factors(n):
    pf = []
    seq = []
    factors = get_factors(n)
    for factor in factors:
        if is_prime(factor):
            pf.append(factor)
    while len(pf):
        prime = pf.pop()
        n /= prime
        seq.append(prime)
    if n > 0:
        if n in seq:
            seq[seq.index(n)] *= 2
    return seq

consecutive = 0
i = 647
found = []

while consecutive < 4:
    i += 1
    factors = get_prime_factors(i)
    if len(factors) == 4:
        unique = True
        for factor in factors:
            if factor in found:
                consecutive = 0
                unique = False
                found = []
                break
    else:
        unique = False
    if unique:
        found += factors
        consecutive += 1

print i
