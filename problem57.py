def next_expansion(n, d):
    n, d = n + d * 2, n + d
    return n, d

n = 3
d = 2
total = 0
for i in xrange(1000):
    n, d = next_expansion(n, d)
    if len(str(n)) > len(str(d)):
        total += 1

print total
