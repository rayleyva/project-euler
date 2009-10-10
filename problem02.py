a, b, s = 1, 0, 0
while s < 4000000:
    a, b = a+b, a
    if a % 2 == 0:
        s += a

print s
