#!/usr/bin/env python3

import sys
import operator

from typing import List, Tuple


class Equation:
    def __init__(self, target: int, numbers: List[int]):
        self.target = target
        self.numbers = numbers

    def __str__(self) -> str:
        return '{}: {}'.format(self.target, ' '.join([str(x) for x in self.numbers]))

    def __bool__(self) -> bool:
        return self._recursive_test(1, self.numbers[0])

    def _recursive_test(self, idx: int, sum: int):
        if sum > self.target:
            return False
        if idx == len(self.numbers):
            return sum == self.target
        return self._recursive_test(idx + 1, sum + self.numbers[idx]) or \
                self._recursive_test(idx + 1, sum * self.numbers[idx]) or \
                self._recursive_test(idx + 1, int(str(sum) + str(self.numbers[idx]))) # Only for part 2


def parse(line: str) -> Tuple[int, List[int]]:
    a = line.strip().split(':')
    b = a[1].strip().split(' ')
    return (int(a[0]), [int(x) for x in b])


with open(sys.argv[1]) as f:
    equations = [Equation(*parse(line)) for line in f]

s = 0
for e in equations:
    if e:
        s += e.target
print(s)
