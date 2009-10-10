import math

def is_prime(n):
    if n < 0:
        return False
    for j in range(2, math.sqrt(n)+1):
        if n%j == 0:
            return False
    return True

big = 600851475143

i = 1

while i*i <= big:
    i += 2
    if big % i == 0:
        if is_prime(i):
            maximum = i

print maximum
