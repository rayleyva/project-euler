import math

def is_prime(n):
    if n < 2:
        return False
    for j in range(2, math.sqrt(n)+1):
        if n%j == 0:
            return False
    return True

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    orig = n = str(n)
    while len(n) > 1:
        n = n[:-1]
        if not is_prime(int(n)):
            return False
    n = orig
    while len(n) > 1:
        n = n[1:]
        if not is_prime(int(n)):
            return False
    return True

# primes or odd numbers will be considered valid digits
valid_digits = [1, 2, 3, 5, 7, 9]

# seed it with the valid ones
possibles = list(valid_digits)

# generate numbers and check for their 'truncatable-ness'
found = []

while len(found) < 11:
    new_possibles = []
    for i in xrange(len(possibles)):
        last_digit = possibles[i] % 10
        first_digit = int(str(possibles[i])[0])
        for digit in valid_digits:
            new_possibles.append(int(str(possibles[i]) + str(digit)))
            new_possibles.append(int(str(digit) + str(possibles[i])))
                
    possibles = []
    
    for num in new_possibles:
        if num not in found and is_truncatable_prime(num):
            found.append(num)
        if is_prime(num):
            possibles.append(num)

print sum(found)
