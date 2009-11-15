def is_palindrome(num):
    return str(num) == str(reverse(num))

def reverse(num):
    return int(str(num)[::-1])

max_iters = 50
lychrels = 0

for i in xrange(1, 10001):
    done = False
    j = 0
    num = i
    while not done and j < max_iters:
        num = num + reverse(num)
        if is_palindrome(num):
            done = True
        j += 1
    if not done:
        lychrels += 1

print lychrels
