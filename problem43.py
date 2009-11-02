def generate_perms(nums):
    if len(nums) <=1:
        yield nums
    else:
        for perm in generate_perms(nums[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + nums[0:1] + perm[i:]

found = []
multiples = [17, 13, 11, 7, 5, 3, 2]
nums = '1234567890'
size = 10

for num in generate_perms(nums):
    if num[0] == '0':
        continue
    matches = True
    for i in range(len(multiples)):
        val = int(num[10-3-i:10-i])
        if val % multiples[i] != 0:
            matches = False
            break
    if matches:
        found.append(int(num))

print sum(found)
