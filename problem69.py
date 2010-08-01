# euler's totient function f(n) gives count of numbers less than n
# which are relatively prime to n.  find the maximum n/f(n) for n <= 1M.
# taking n * (1 - 1/x) for all x that are distinct prime factors
#
# http://en.wikipedia.org/wiki/Euler%27s_totient_function
import math

def is_prime(n):
    if n < 2:
        return False
    elif n != 2 and n % 2 == 0:
        return False
    for i in xrange(3, math.sqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

# since 1M = 1000**2, we'll only be dealing with prime factors less
# than 1000
primes = [p for p in xrange(1001) if is_prime(p)]
primes = set(primes)

def prime_factors(n, primes):
    factors = set([])
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            factors.add(p)
    return factors

def eulers_totient(n, primes):
    pf = prime_factors(n, primes)
    p = n
    for f in pf:
        p *= (1 - (1.0 / f))
    return p

max_ratio = 0, 0

for n in xrange(1, 1000001):
    et = eulers_totient(n, primes)
    ratio = n / et
    if ratio > max_ratio[1]:
        max_ratio = n, ratio

print max_ratio
