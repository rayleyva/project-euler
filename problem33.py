num = denom = 1
for i in range(10, 100):
    for j in range(i + 1, 100):
        i, j = float(i), float(j)
        if i % 10 != 0 and j % 10 != 0:
            num_lt, num_rt = divmod(i, 10)
            denom_lt, denom_rt = divmod(j, 10)
            if i / j == num_lt / denom_rt and num_rt == denom_lt:
                print '%d * %d = %d * %d' % (i, j, num_lt, denom_rt)
                num *= i
                denom *= j
print denom / num
