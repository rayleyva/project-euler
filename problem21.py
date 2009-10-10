import math

def proper_divisors(n):
    d = []
    d.append(1)
    for j in range(2, math.sqrt(n) + 1):
        if n % j == 0:
            d.append(j)
            d.append(n/j)
    return set(d)

divisors = []

# generate a list of the sum of proper divisors for all number 1 to 9999
for i in range(0, 10000):
    divisors.append(sum(proper_divisors(i)))

# iterate over list of sums of divisors, first getting the value of the sum of divisors for a number i and storing it in a
# then, if a is less than 10000, get the sum of divisors for a.  compare original input i with b to see if they are the same,
# make sure a != b (which would be a 'perfect' number)
total = 0
for i in range(0, 10000):
    a = divisors[i]
    if a < 10000:
        b = divisors[a]
        if i == b and a != b:
            print ('%d and %d are amicable' % (a, b))
            total += a
print total
