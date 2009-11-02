digits = [10**i for i in xrange(7)]

s = ''
i = 0
while len(s) <= max(digits):
    i += 1
    s += str(i)

p = 1
for digit in digits:
    p *= int(s[digit - 1])

print p
