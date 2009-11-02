import math

def is_right_triangle(a, b, c):
    if not a <= b or not b < c:
        return False
    if a**2 + b**2 == c**2:
        return True
    return False

def solve_triangle(perimeter):
    max_a = perimeter / 3
    max_b = perimeter / 2
    triangles_found = 0
    for a in xrange(1, max_a + 1):
        for b in xrange(a, max_b + 1):
            c = perimeter - a - b
            if is_right_triangle(a, b, c):
                triangles_found += 1
    return triangles_found

perimeter = max_found = 0

for i in xrange(2, 1001):
    triangles_found = solve_triangle(i)
    if triangles_found > max_found:
        max_found = triangles_found
        perimeter = i

print "Perimeter %d returns %d triangles" % (perimeter, max_found)
