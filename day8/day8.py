#!/usr/bin/env python3
import sys

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x + 10000 * self.y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

def inbounds(vec, width, height):
    return vec.x >= 0 and vec.y >= 0 and vec.x < width and vec.y < height

#  x -->
# y
# |
# v
def antennas(map):
    a = {}
    for y, line in enumerate(map):
        for x, ch in enumerate(line):
            if ch not in ".\n":
                if ch in a:
                    a[ch].append(Vector(x, y))
                else:
                    a[ch] = [Vector(x, y)]
    return a, len(map[0]), len(map)

def p(map, antinodes):
    s = []
    for i in range(w):
        s.append(['.' for i in range(h)])
    for antenna, coords in map.items():
        for c in coords:
            s[c.y][c.x] = antenna
    for c in antinodes:
            s[c.y][c.x] = "#"
    return '\n'.join([''.join(x) for x in s])

with open(sys.argv[1]) as f:
    map, w, h = antennas([x.strip() for x in f.readlines()])

antinodes = set()
antinodes2 = set()
for antenna, coords in map.items():
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            a = coords[i]
            b = coords[j]
            v = b - a
            # Part 1
            p1 = b + v
            p2 = a - v
            if inbounds(p1, w, h):
                antinodes.add(p1)
            if inbounds(p2, w, h):
                antinodes.add(p2)
            # Part 2
            antinodes2.add(a)
            antinodes2.add(b)
            while inbounds(p1, w, h):
                antinodes2.add(p1)
                p1 = p1 + v
            while inbounds(p2, w, h):
                antinodes2.add(p2)
                p2 = p2 - v
print(len(antinodes))
print(len(antinodes2))
#print(p(map, antinodes2))
