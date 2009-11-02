def sum_word(word):
    return sum(map(lambda x: (ord(x) - 64), word))

triangles = [1]
for i in range(2, 20):
    triangles.append(i + triangles[i - 2])

total = 0

f = open("words.txt", "r")
words = f.read()
words = words.replace('"', '')
words = words.split(',')
for word in words:
    if sum_word(word) in triangles:
        total += 1

print total
