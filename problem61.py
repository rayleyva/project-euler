import math

def triangle(n):
    return ((n * n) + n) / 2

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

nums = []

# build a list of all numbers that pass one of the tests
for i in xrange(1000, 10000):
    if is_triangle(i)   or \
       is_square(i)     or \
       is_pentagonal(i) or \
       is_hexagonal(i)  or \
       is_heptagonal(i) or \
       is_octagonal(i):
        nums.append(i)

# a list of tests our numbers need to pass
tests_available = [is_triangle, is_square, is_pentagonal, is_hexagonal, 
                   is_heptagonal, is_octagonal]

def test_nums(all_nums, matches, tests_remaining):
    if len(matches) > 0:
        # if we've got a matching number already, filter down the numbers we
        # iterate over to ones whose first two digits will be the last two of
        # the previous number
        min_match = int(str(matches[-1])[2:]) * 100
        max_match = min_match + 100
    else:
        min_match = max_match = None
    # if a matches last two started with a zero, bail out
    if len(matches) and not min_match > 1000: return
    
    # iterate over all numbers
    for num in all_nums:
        # if we have a match condition and number is in range, or if this is the
        # first go-round
        if (min_match and num > min_match and num < max_match) or not min_match:
            for i, test in enumerate(tests_remaining):
                if test(num):
                    # if we're down to our last test and the number we're
                    # looking at completes the sequence, print them out!
                    if len(tests_remaining) == 1 and \
                       int(str(num)[2:]) == int(str(matches[0])[:2]):
                        print matches + [num]
                        print sum(matches + [num])
                        return
                    else:
                        # call it recursively
                        test_nums(all_nums, matches + [num], 
                                  tests_remaining[:i] + tests_remaining[i+1:])
        elif (min_match and num > max_match):
            # we can safely get out of here now
            return
test_nums(nums, [], tests_available)
