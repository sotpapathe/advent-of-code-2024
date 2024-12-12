#!/usr/bin/env python3
import sys
import re

with open(sys.argv[1]) as f:
    str = ''.join(f.readlines())

# Part 1
prog = re.compile('mul\([0-9]{1,3},[0-9]{1,3}\)')
r = prog.findall(str)
s = 0
for m in r:
    m = m.strip('mul()')
    m = m.split(',')
    s += int(m[0]) * int(m[1])
print(s)

# Part 2
prog = re.compile("(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))")
r = prog.findall(str)
s = 0
do = True
for m in r:
    if m.startswith('don'):
        do = False
        continue
    elif m.startswith('do'):
        do = True
        continue
    if do:
        m = m.strip('mul()')
        m = m.split(',')
        s += int(m[0]) * int(m[1])
print(s)
