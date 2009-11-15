def fac(n):
    if n < 1:
        return 1
    else:
        return n * fac(n - 1)

def C(n, r):
    return (fac(n) / (fac(r) * fac(n - r)))

found = []
for n in xrange(23, 101):
    for r in xrange(1, n):
        if C(n, r) > 1000000:
            found.append((n, r))

print len(found)
