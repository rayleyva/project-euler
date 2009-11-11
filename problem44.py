import math

def pentagonal(n):
    return (n * ((3 * n) - 1)) / 2

def is_pentagonal(n):
    # solve the quadratic
    # 0 = 3x**2 - x - 2n
    return (1 + math.sqrt(1 + (24 * n))) % 6 == 0

found = False
pentagonals = map(pentagonal, range(1, 10000))
print "Finished mapping pentagonal numbers %s...%s" % (pentagonals[0], pentagonals[-1])
for i in range(len(pentagonals)):
    for j in range(i, 0, -1):
        if (pentagonals[i] - pentagonals[j]) in pentagonals and \
           (pentagonals[i] + pentagonals[j]) in pentagonals:
            print pentagonals[i] - pentagonals[j]
            found = True
    if found:
        break
