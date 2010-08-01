fh = open('triangle.txt', 'r')

lines = fh.readlines()
flattened = [[int(lines[0])]]

for i, row in enumerate(lines[1:]):
    row = map(int, row.split())
    flattened_row = []
    for j, num in enumerate(row):
        if j > 0:
            top_l = j - 1
        else:
            top_l = j
        if j < len(flattened[i]):
            top_r = j
        else:
            top_r = top_l
        num_l = flattened[i][top_l]
        num_r = flattened[i][top_r]
        flattened_row.append(max(num + num_l, num + num_r))
    flattened.append(flattened_row)
print max(flattened_row)
