import math

def is_prime(n):
    for j in range(2, math.sqrt(n)+1):
        if n%j == 0:
            return False
    return True

valid_digits = [3, 7, 9]
possibles = valid_digits

# for argument's sake say the biggest
# number is 7 digits long
for i in range(3):
    new_ones = []
    for possible in possibles:
        for valid_digit in valid_digits:
            new_ones.append(int(str(possible) + str(valid_digit)))
    possibles += new_ones

possibles = set(possibles)

primes = 0

for possible in possibles:
    if is_prime(possible):
        primes += 1

print primes
