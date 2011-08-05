#!/usr/bin/env python

bits = {}

for login in file('keylog.txt'):
    login = str(int(login))
    for i, digit in enumerate(login[:-1]):
        if digit not in bits:
            bits[digit] = []
        for rest in login[i+1:]:
            if rest not in bits[digit]:
                bits[digit].append(rest)
            if rest not in bits:
                bits[rest] = []

print bits
for digit, _ in sorted(bits.items(), key=lambda (k,v):len(v), reverse=True):
    print digit,
