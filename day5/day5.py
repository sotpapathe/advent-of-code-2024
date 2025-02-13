#!/usr/bin/env python3
import sys

from typing import List, Tuple, Any


def gen_rule(a: int, b: int):
    class F:
        def __call__(self, l: List[int]) -> bool:
            try:
                ia = l.index(a)
            except ValueError:
                return True
            try:
                ib = l.index(b)
            except ValueError:
                return True
            return ia < ib

        def __repr__(self) -> str:
            return "{}|{}".format(a, b)

        def swap(self, l: List[int]) -> None:
            if not self(l):
                ia = l.index(a)
                ib = l.index(b)
                l[ia], l[ib] = b, a

    return F()


def parse_rule(line: str) -> Tuple[Any, int, int]:
    n = [int(x) for x in line.split('|')]
    return gen_rule(n[0], n[1]), n[0], n[1]


def check_rules(l: List[int], rules: List[Any]) -> Tuple[bool, List[Any]]:
    valid = True
    failed_rules = []
    for r in rules:
        if not r(l):
            valid = False
            failed_rules.append(r)
    return valid, failed_rules


rules = []
page_lists = []
with open(sys.argv[1]) as f:
    in_rules = True
    for line in f:
        line = line.strip()
        if line == '':
            in_rules = False
            continue
        if in_rules:
            f, n1, n2 = parse_rule(line)
            rules.append(f)
        else:
            page_lists.append([int(x) for x in line.split(',')])

s_valid = 0
s_invalid = 0
for l in page_lists:
    first_try = True
    converged = False
    while not converged:
        valid, failed_rules = check_rules(l, rules)
        if valid:
            converged = True
        else:
            first_try = False
            for r in failed_rules:
                r.swap(l)
    idx = l[int(len(l)/2)]
    if first_try:
        s_valid += idx
    else:
        s_invalid += idx
print("valid:", s_valid)
print("invalid:", s_invalid)
