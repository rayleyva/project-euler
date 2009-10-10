total = 1
n = 1
delta = 2
x = 1
# width = n * 2 + 1
# step = n * 2
# desired width = 1001 = (500 * 2) + 1
for i in range(0, 500):
    x += delta
    step = n * 2
    total += sum([z for z in range(x, x + (4*step) - 1, step)])
    delta += 8
    n += 1
print total
