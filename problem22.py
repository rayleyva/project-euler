def name_score(name):
    score = 0
    for char in name:
        score += ord(char) - ord('A') + 1
    return score

f = open("names.txt", "r")
names = f.read()
names = names.replace('"', '')
names = names.split(',')
names.sort()
s = 0
for i in range(len(names)):
    score = name_score(names[i]) * (i + 1)
    s += score

print s
