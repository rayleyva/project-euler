import math

def pentagonal(n):
    return (n * ((3 * n) - 1)) / 2

def is_pentagonal(n):
    # solve the quadratic
    # 0 = 3x**2 - x - 2n
    return (1 + math.sqrt(1 + (24 * n))) % 6 == 0

def hexagonal(n):
    return (2*n*n - n)

def is_hexagonal(n):
    return (1 + math.sqrt(1 + (8 * n))) % 4 == 0

def triangle(n):
    return (n*n + n) / 2

def is_triangle(n):
    return (-1 + math.sqrt(1 + (8 * n))) % 2 == 0

start = 40755
hex_seed = (1 + math.sqrt(1 + (8 * 40755))) / 4

found = False

while not found:
    hex_seed += 1
    num = hexagonal(hex_seed)
    if is_pentagonal(num) and is_triangle(num):
        print "Result: %d" % num
        found = True
