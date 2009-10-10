import math

# this method is very slow - improve using a prime sieve
def is_prime(n):
    for j in range(2, math.sqrt(n)+1):
        if n%j == 0:
            return False
    return True

s = 2 # add 2 to start, since looping over odd #s
for i in range(3, 2000000, 2):
    if is_prime(i):
        s += i

print s
