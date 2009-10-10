# pretty slow
def perm(S, perms=[], current=[], maximum=None):
    if maximum and len(perms) > maximum:
        return
    size = len(S)
    for i in range(size):
        subset = list(S)
        del(subset[i])
        tmp_current = list(current)
        tmp_current.append(S[i])
        if size > 1:
            perm(subset, perms, tmp_current, maximum)

        else:
            perms.append(tmp_current)
            if maximum:
                if len(perms) == maximum:
                    print tmp_current
                    return

perm('0123456789', maximum=1000000)
