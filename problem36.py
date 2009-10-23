def is_palindrome(num):
    return str(num) == str(num)[::-1]

def to_binary(num):
    b = ''
    while num > 0:
        b = str(num % 2) + b
        num /= 2
    return b

x = 999999
total = 0
while x >= 1:
     if is_palindrome(x) and is_palindrome(to_binary(x)):
        total += x
     x -= 2 # can't be even since this would cause binary to end in zero
     
print total
