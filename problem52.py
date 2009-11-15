def same_nums(a, b):
    a = list(str(a))
    b = list(str(b))
    for num in a:
        exists = False
        for j in xrange(len(b)):
            if b[j] == num:
                del(b[j])
                exists = True
                break
        if not exists:
            return False
    if len(b) == 0:
        return True
    else:
        return False

done = False
i = 1
while not done:
    matches = True
    for j in xrange(2, 7):
        if not same_nums(i, i*j):
            matches = False
            break
    if matches:
        print i
        done = True
    i += 1
