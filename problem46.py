import math

def is_prime(n):
    if n < 2:
        return False
    for j in range(2, math.sqrt(n) + 1):
        if n%j == 0:
            return False
    return True

primes = [2] # since iterating over odd nums
found = False
i = 3
while not found:
    if is_prime(i):
        primes.append(i)
    else:
        match_found = False
        for n in primes:
            difference = i - n
            if difference % 2 == 0:
                possible_square = difference / 2
                j = 1
                not_found = True
                while j*j <= possible_square:
                    if j*j == possible_square:
                        match_found = True
                        break
                    j += 1
            if match_found:
                break
        if not match_found:
            print "%d" % i
            found = True
    i += 2 # check odd numbers
