# 1*2345=2345  <-- using 9 digits
# 12*345=4140  <-- using 9 digits
# 99*999=98901 <-- too many

digits = '123456789'

def generate_perms(nums):
    if len(nums) <=1:
        yield nums
    else:
        for perm in generate_perms(nums[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + nums[0:1] + perm[i:]

products = []
for perm in generate_perms(digits):
    if int(perm[:1]) * int(perm[1:5]) == int(perm[5:]):
        print "%d * %d = %d" % (int(perm[:1]), int(perm[1:5]), int(perm[5:]))
        products.append(int(perm[5:]))
    if int(perm[:2]) * int(perm[2:5]) == int(perm[5:]):
        products.append(int(perm[5:]))
        print "%d * %d = %d" % (int(perm[:2]), int(perm[2:5]), int(perm[5:]))

print sum(set(products))
