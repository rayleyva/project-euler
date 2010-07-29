#!/usr/bin/python
# solve x^2 - Dy^2 = 1 for minimum x, where D <= 1000 -- what is maximum x?
import math

squares = [x**2 for x in xrange(50)]
seen = {}

largest_x = 0
max_d = 100

for d in xrange(1, max_d + 1):
    if d in squares:
        continue
    
    x = 1
    x_done = False
    
    while not x_done:
        x += 1
        while True:
            y_target, r = divmod((x**2 - 1), d)
            if (r):
                x += 1
            else:
                y_root = math.sqrt(y_target)
                if y_root**2 == int(y_root)**2:
                    print x, d, y_root
                    x_done = True
                    break
                else:
                    x += 1

    if x > largest_x:
        largest_x = x

print largest_x 
