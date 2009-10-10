def lowest_evenly_divisible(num):
    found = False
    store = num
    while not found:
        num += store # note that I'm not increasing by 1, but by the search number itself
        flag = True
        j = store - 1 
        # test against all numbers 2..store - 1     
        # don't need to test against store since we already know it is a factor   
        while j > 1:
            if num % j != 0:
                flag = False # doesn't divide easily, so break and try next num in sequence
                break
            j -= 1
        if flag:
            return num

print lowest_evenly_divisible(20) # prints 232792560 
