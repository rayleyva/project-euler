max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        cur_sum = sum([int(x) for x in str(a**b)])
        if cur_sum > max_sum:
            max_sum = cur_sum
print max_sum
