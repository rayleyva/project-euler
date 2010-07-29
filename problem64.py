#!/usr/bin/python

# the idea is that a square root can be expressed as a continued fraction,
# so that sqrt(n) = 1 + 1/x
# - find all square roots 1 < n <= 10000 whose period is odd
#
# useful links:
# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#sqrtcf

import math


def repetition(nums):
    l = len(nums)
    for i in xrange(l / 2):
        cur = nums[:i+1]
        times = l / (i+1)
        if cur * times == nums:
            return i + 1
    
    return 0

odd = 0
largest = 0

for s in xrange(1, 10001):
    a = a0 = int(math.sqrt(s))
    
    if a * a == s:
        # ignore perfect squares
        continue

    m = 0
    d = 1
    buf = []
    count = 0
    while True:
        m = d * a - m
        d = (s - m**2) / d
        a = int((a0 + m) / d)
        buf.append(a)
        
        if len(buf) > 100:
            r = repetition(buf)
            if r % 2 != 0:
                odd += 1
            if r:
                break

print odd
