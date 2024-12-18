#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as f:
    letters = [x.strip() for x in f.readlines()]
c = 0
