import math

def is_prime(n):
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for j in xrange(3, math.sqrt(n) + 1, 2):
        if n % j == 0:
            return False
    return True

def get_digits(n):
    return map(lambda x: int(x), set(list(str(n))))

def repl_digit(n, old, new):
    return int(str(n).replace(str(old), str(new)))

done = False
i = 11 # start with 11 since we know it's not a 1-digit num
while not done:
    if is_prime(i):
        for digit in get_digits(i):
            found = [i]
            for repl in xrange(0, 10):
                if repl != digit:
                    possible = repl_digit(i, digit, repl)
                    if is_prime(possible) and len(str(possible)) == len(str(i)):
                        found.append(possible)
            if len(found) == 8:
                print found
                done = True
    i += 2
