def fac(n):
    if n > 1:
        return n * fac(n - 1)
    return 1

print sum([int(char) for char in str(fac(100))])
