def val_at_pos(n):
    # 1-9:          9       (9 * 1)
    # 10-99:        180     (90 * 2)
    # 100-999:      2700    (900 * 3)
    # ...
    cutoffs = []
    for i in xrange(6):
        cutoffs.append((10**i * 9) * (i + 1))
        if n < sum(cutoffs[:i + 1]):
            cutoff = i
            break
    
digits = [10**i for i in xrange(7)]

