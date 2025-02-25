#!/usr/bin/env python3
import copy
import sys


class Guard:
    normals = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, pos):
        self.pos = pos
        self.dir = 0
        self.path = set()
        self.start_pos = pos

    def next(self):
        n = Guard.normals[self.dir]
        return (self.pos[0] + n[0], self.pos[1] + n[1])

    def step(self, region):
        nextp = self.next()
        try:
            ch = region[nextp[0]][nextp[1]]
            if ch in ['.', 'X']:
                self.path.add((self.pos, self.dir))
                self.pos = nextp
                region[self.pos[0]][self.pos[1]] = 'X'
            elif ch in ['#', 'O']:
                self.dir = (self.dir + 1) % len(Guard.normals)
            return True
        except IndexError:
            return False

    def loop(self, region) -> bool:
        nextp = self.next()
        if nextp == self.start_pos:
            return False
        tmpregion = copy.deepcopy(region)
        try:
            tmpregion[nextp[0]][nextp[1]] = 'O'
        except IndexError:
            return False

        tmpguard = Guard(self.start_pos)
        while True:
            if tmpguard._looped():
                p(tmpregion)
                return True
            if not tmpguard.step(tmpregion):
                break
        return False

    def _looped(self) -> bool:
        return (self.pos, self.dir) in self.path


def p(region):
    print('\n\n')
    for i, line in enumerate(region):
        print('{:3d} {}'.format(i, ''.join(line)))

def split(line):
    return [x for x in line]

def countX(region) -> int:
    s = 0
    for line in region:
        for ch in line:
            if ch == 'X':
                s += 1
    return s


with open(sys.argv[1]) as f:
    region = [split(x.strip()) for x in f.readlines()]

for r, row in enumerate(region):
    for c, ch in enumerate(row):
        if ch == '^':
            pos = (r, c)
            region[r][c] = 'X'

obstacles = set()
guard = Guard(pos)
while True:
    print(len(guard.path), end='\r')
    if guard.loop(region):
        obstacles.add(guard.next())
    if not guard.step(region):
        break
p(region)
print("positions", countX(region))
print("loops", len(obstacles))
# 2024 obstacles are too high
# 1000 obstacles are too low
