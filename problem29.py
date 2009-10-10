# distinct terms in a^b for all a in range(2, 101), b in range(2, 101)
nums = []
for a in range(2, 101):
    for b in range(2, 101):
        nums.append(a**b)

print len(set(nums))
