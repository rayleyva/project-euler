import math
# function to generate a set of the proper divisors for a given numer
def proper_divisors(n):
    d = []
    d.append(1)
    for j in range(2, math.sqrt(n) + 1):
        if n % j == 0:
            d.append(j)
            d.append(n/j)
    return set(d)

def generate_abundant(n):
    abundant = []
    for i in range(1, n+1):
        sum_pds = sum(proper_divisors(i))
        if sum_pds > i:
            abundant.append(i)
    return abundant

ab = generate_abundant(28124)
sums = set()

for i in range(len(ab)):
    for j in range(i, len(ab)):
        k = ab[i] + ab[j]
        if k < 28124:
            sums.add(k)

print sum(set(range(28124)).difference(sums))
