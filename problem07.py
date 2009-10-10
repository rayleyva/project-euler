import math

def is_prime(n):
    if n < 0:
        return False
    for j in range(2, math.sqrt(n)+1):
        if n%j == 0:
            return False
    return True

primes = []
i = 1

while len(primes) <= 10000:
    i += 1
    if is_prime(i):
        primes.append(i)

print i
