#!/usr/bin/env python3

import sys
import operator

from typing import List, Tuple


class Equation:
    OPERATORS = [operator.add, operator.mul]

    def __init__(self, target: int, numbers: List[int]):
        self.target = target
        self.numbers = numbers

    def __str__(self) -> str:
        return '{}: {}'.format(self.target, ' '.join([str(x) for x in self.numbers]))

    def __bool__(self) -> bool:
        # TODO: recurse
        pass


def parse(line: str) -> Tuple[int, List[int]]:
    a = line.strip().split(':')
    b = a[1].strip().split(' ')
    return (int(a[0]), [int(x) for x in b])


with open(sys.argv[1]) as f:
    equations = [Equation(*parse(line)) for line in f]

for e in equations:
    print(e)
