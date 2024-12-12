#!/usr/bin/env python3
import sys

a = []
b = []
with open(sys.argv[1]) as f:
    for line in f:
        c = line.split()
        a.append(int(c[0]))
        b.append(int(c[1]))
a.sort()
b.sort()

s = 0
for i in range(len(a)):
    s += abs(a[i] - b[i])

# Part 1
print(s)

hash = {}
for elem in b:
    if elem in hash:
        hash[elem] += 1
    else:
        hash[elem] = 1

s = 0
for elem in a:
    if elem in hash:
        s += elem * hash[elem]

# Part 2
print(s)
