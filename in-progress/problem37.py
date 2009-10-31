import math

def is_prime(n):
    for j in range(2, math.sqrt(n)+1):
        if n%j == 0:
            return False
    return True

valid_digits = [3, 7, 9]
possibles = [3, 7, 9]

# create a bunch of 
i = 0
for i in range(6):
    for i in range(len(possibles)):
        for valid_digit in valid_digits:
            possibles.append(int(str(possibles[i]) + str(valid_digit)))

possibles = set(possibles)
primes = 0
primes = []

for possible in possibles:
    if is_prime(possible):
        primes.append(possible)


