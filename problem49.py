import math

def is_prime(n):
    if n < 2:
        return False
    for j in range(2, math.sqrt(n) + 1):
        if n%j == 0:
            return False
    return True

def generate_perms(nums):
    if len(nums) <=1:
        yield nums
    else:
        for perm in generate_perms(nums[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + nums[0:1] + perm[i:]

for i in xrange(1001, 10000, 2):
    if is_prime(i):
        prime_perms = {}
        for perm in generate_perms(str(i)):
            perm = int(perm)
            if perm < 1000:
                continue
            if is_prime(perm) and perm != i:
                prime_perms[perm] = abs(perm - i)
        if len(prime_perms) > 1:
            differences = prime_perms.values()
            diffs = {}
            for diff in differences:
                if diffs.has_key(diff):
                    diffs[diff] += 1
                    if diffs[diff] > 1:
                        print "%s %s (%s)" % (i, [x for x in prime_perms if prime_perms[x] == diff], diff)
                else:
                    diffs[diff] = 1
