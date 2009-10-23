import math

def is_prime(n):
    for j in range(2, math.sqrt(n)+1):
        if n%j == 0:
            return False
    return True

primes = []
i = 1

while i < 1000000:
    i += 1
    if is_prime(i):
        primes.append(i)

print "Primes generated: %d" % len(primes)

total = 0
circular = []

for p in primes:
    if '0' not in str(p):
        # roll through
        is_circular = True
        tmp_circular = [p]
        if p > 10 and p not in circular:
            for i in range(1, len(str(p))):
                p = int(str(p)[1:] + str(p)[0])
                if p not in primes:
                    is_circular = False
                    break
                else:
                    tmp_circular.append(p)
        if is_circular:
            circular += tmp_circular
            total += 1

print total
