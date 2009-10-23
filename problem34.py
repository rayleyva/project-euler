factorial_cache = [1]
for n in range(1, 10):
    factorial_cache.append(factorial_cache[n - 1] * n)

# trick is to find the maximum possible number it could be
# 9! = 362880
# 362880 * 7 < 10**7 - 1
# but here's the code anyway:
max_digit = factorial_cache[9]
n = 1
while max_digit * n > (10**n - 1):
    n += 1

total = 0

for i in range(3, (max_digit * n)):
    digits = list(str(i))
    digit_sum = sum([factorial_cache[int(n)] for n in digits])
    if i == digit_sum:
        print '%s! = %d' % ('! + '.join(digits), digit_sum)
        total += digit_sum

print "Total: %d" % (total)
