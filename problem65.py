# e can be expressed as a continued fraction of the form
# [2;1,2,1,1,4,1,...1,2k,1,...]

def get_nums(amount):
    i = 1
    nums = [2]
    while len(nums) < amount:
        nums.extend([1, 2 * i, 1])
        i += 1
    return nums[:amount]

nums_to_calculate = 100
a = 2
nums = get_nums(nums_to_calculate)

numerator = 1
denominator = nums[nums_to_calculate - 1]

for i in xrange(nums_to_calculate, 1, -1):
    prev_num = nums[i - 2]
    if denominator != 1:
        prev_num *= denominator
    combined_num = prev_num + numerator
    numerator = denominator
    denominator = combined_num

print sum(int(d) for d in str(combined_num))
