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

target = 1000000 # this is the max sum

cur_sequence = 0
max_sequence = 0
cur_sum = 0
max_sum = 0

# the highest number we should check is going to be approx
# 1,000,000 divided by the max number of items in the longest
# sequence, so guess the smallest number expected
min_expected = 100

done = False
primes = [2]
i = 3
while i < (target / min_expected):
    if is_prime(i):
        primes.append(i)
    i += 2

working_list = list(primes)

i = 0
while i < (len(primes) - max_sequence):
    cur_sum = primes[i]
    for j in xrange(len(primes) - 1, i, -1):
        if sum(primes[i:j]) < target:
            if is_prime(sum(primes[i:j])):
                cur_sequence = j - i
                cur_sum = sum(primes[i:j])
                break
    if cur_sequence > max_sequence:
        max_sequence = cur_sequence
        max_sum = cur_sum
    i += 1

print '%d: %d' % (max_sum, max_sequence)
