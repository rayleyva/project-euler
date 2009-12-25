import math

def triangle(n):
    return (n*n + n) / 2

def is_triangle(n):
    return (-1 + math.sqrt(1 + (8 * n))) % 2 == 0

def square(n):
    return n*n

def is_square(n):
    return int(math.sqrt(n)) == math.sqrt(n)

def pentagonal(n):
    return (n * ((3 * n) - 1)) / 2

def is_pentagonal(n):
    return (1 + math.sqrt(1 + (24 * n))) % 6 == 0

def hexagonal(n):
    return (2*n*n - n)

def is_hexagonal(n):
    return (1 + math.sqrt(1 + (8 * n))) % 4 == 0

def heptagonal(n):
    return (n * (5 * n - 3)) / 2

def is_heptagonal(n):
    return (3 + math.sqrt(9 + (40 * n))) % 10 == 0

def octagonal(n):
    return (n * (3 * n - 2))

def is_octagonal(n):
    return (2 + math.sqrt(4 + (12 * n))) % 6 == 0

triangles = []
squares = []
pentagonals = []
hexagonals = []
heptagonals = []
octagonals = []

for i in xrange(1000, 10000):
    if is_triangle(i):
        triangles.append(i)
    if is_square(i):
        squares.append(i)
    if is_pentagonal(i):
        pentagonals.append(i)
    if is_hexagonal(i):
        hexagonals.append(i)
    if is_heptagonal(i):
        heptagonals.append(i)
    if is_octagonal(i):
        octagonals.append(i)

group = [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]
