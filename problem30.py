# sum of all the numbers that can be written as the sum of fifth powers of their digits.
# abc.. = a^5 + b^5 + c^5 ...
max_digit = 9**5 # 59049
n = len(str(max_digit)) # figure out how long the number is
while (max_digit*n >= 10**n):
    n += 1
max_possible = max_digit * n # 354294
print "Max possible: %d" % max_possible
powers = [x**5 for x in range(0, 10)] # cache powers
found = []
for i in range(2, max_possible):
    ds = str(i)
    tot = 0
    for c in range(0, len(ds)):
        tot += powers[int(ds[c])]
        if tot > i:
            break
    if tot == i:
        found.append(i)

print sum(found)
