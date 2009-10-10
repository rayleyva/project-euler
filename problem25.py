huge_int = int('1%s' % ('0' * 999))

def fib(n):
    a, b = 1, 0
    i = 0
    while a < n:
        a, b = a+b, a
        i += 1
    return i+1

print fib(huge_int)
