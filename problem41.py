import math

def is_prime(n):
    for j in range(2, math.sqrt(n)+1):
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

found = []

nums = ''.join([str(x) for x in range(1, 8)])
for num in generate_perms(nums):
    if is_prime(int(num)):
        found.append(num)

print max(found)
