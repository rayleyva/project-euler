import math

def is_prime(n):
    for j in range(2, math.sqrt(n)+1):
        if n%j == 0:
            return False
    return True

def process_numbers(max_digits=1000):
    maximum = 0
    primes = [x for x in range(3, max_digits, 2) if is_prime(x)]
    for i in primes:
        dividend = 1
        divisor = i
        counter = 0
        quotient = ''
        while counter < max_digits:
            q, r = divmod(float(dividend), float(divisor))
            quotient += str(int(q))
            #print ('%d / %d = %d R%d' % (dividend, divisor, q, r))
            counter += 1
            if r == 0:
                break
            else:
                dividend = r * 10
        if counter > 5:
            part = quotient[counter - 5:counter]
            sample = quotient[:counter-5]
            if part in sample:
                pos = sample.rfind(part)
                diff = (counter - 5) - pos
                if diff > maximum:
                    #print '%d: %d' % (i, diff)
                    maximum = diff
                    biggest = i
    return biggest

print process_numbers()
