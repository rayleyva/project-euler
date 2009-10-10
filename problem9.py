max_a = 332
max_b = 499
max_c = 997

for a in range(1, max_a+1):
     for b in range(1, max_b+1):
         c = 1000 - a - b
         if c > b:
             if (a**2 + b**2)==c**2:
                 print '%d + %d = %d' % (a, b, c) # prints 200 + 375 = 425
                 print 'Product: %d' % (a*b*c) # prints 31875000 
