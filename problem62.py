# first build a dictionary keyed by number=>sorted digits of that number's cube
cube_cache = {}
for i in xrange(10000):
    cube_digits = list(str(i**3))
    cube_digits.sort()
    cube_cache[i] = ''.join(cube_digits)

# second get a list of all the cube digits and sort them
cubes = list(cube_cache.values())
cubes.sort()

def find_cube():
    # iterate over the sorted list of sorted cube digits
    for i, cube in enumerate(cubes):
        # find the one that has 5 matches in a row -- that's our cube!
        if cubes[i:i+5] == [cube] * 5:
            # iterate over the cube cache and print the original number
            for k, v in cube_cache.items():
                if v == cube:
                    print k**3
                    return
                    
find_cube()
