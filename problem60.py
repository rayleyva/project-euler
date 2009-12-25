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

primes = [x for x in xrange(10000) if is_prime(x)]

def test_nums(group):
    for i in xrange(len(group)):
        for j in xrange(len(group)):
            if j != i:
                if not (is_prime(int(str(group[i]) + str(group[j]))) and \
                        is_prime(int(str(group[j]) + str(group[i])))):
                    return False
    return True

def run_test(primes):
    for i in xrange(len(primes) - 5):
        for j in xrange(i + 1, len(primes)):
            if not test_nums([primes[i], primes[j]]):
                continue
            for k in xrange(j + 1, len(primes)):
                if not test_nums([primes[i], primes[j], primes[k]]):
                    continue
                for l in xrange(k + 1, len(primes)):
                    if not test_nums([primes[i], primes[j], primes[k], primes[l]]):
                        continue
                    for m in xrange(l + 1, len(primes)):
                        if not test_nums([primes[i], primes[j], primes[k], primes[l], primes[m]]):
                            continue
                        else:
                            group = [
                                primes[i],
                                primes[j],
                                primes[k],
                                primes[l],
                                primes[m]
                            ]
                            print group
                            print sum(group)
                            return

# remove 2 & 5
primes = primes[1:]
del(primes[1])

print "Testing approx %d combinations" % (len(primes)**5)
run_test(primes)
