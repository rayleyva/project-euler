import math

def is_prime(n):
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for j in xrange(3, math.sqrt(n) + 1, 2):
        if n % j == 0:
            return False
    return True
    
count = 1
primes = 0
delta = 2
x = 1

done = False
while not done:
    corners = [x + (i + 1) * delta for i in xrange(4)]
    count += 4
    for num in corners:
        if is_prime(num):
            primes += 1
    x = corners[3]
    ratio = float(primes) / count
    if ratio < .1:
        done = True
        print delta + 1
    delta += 2
