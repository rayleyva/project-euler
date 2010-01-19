count = 0
i = 1
# 10**x is always x+1 digits long
# 9**1 = 9, 1-digit long,
# 9**2 = 81, 2-digits long
# 9**3 = 729, 3-digits long
# ...so when 9**x goes below x digits long, no more powers will be possible
while len(str(9**i)) >= i:
    done = False
    j = 1
    while not done:
        if len(str(j**i)) == i:
            count += 1
        elif len(str(j**i)) > i:
            done = True
        j += 1
    i += 1
print count
