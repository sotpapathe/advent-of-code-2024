#!/usr/bin/env python3
import sys

def valid_seq(c):
    for i in range(len(c) - 1):
        d = c[i + 1] - c[i]
        if i == 0:
            sign = d > 0
        elif (d > 0) != sign:
            break
        if abs(d) > 3 or d == 0:
            break
        if i == len(c) - 2:
            return True
    return False


def valid_seq2(c):
    sign = None
    num_inc_sign = 0
    num_inc_abs = 0
    for i in range(len(c) - 1):
        d = c[i + 1] - c[i]
        if abs(d) > 3 or d == 0:
            num_inc_abs += 1
            continue
        if sign is None:
            sign = d > 0
        elif (d > 0) != sign:
            num_inc_sign += 1
    if num_inc_abs > 1:
        return False
    if num_inc_abs == 1 and num_inc_sign == 0:
        return True
    if num_inc_sign > 1 or num_inc_sign < len(c) - 1:
        return False
    return True


def subseq(c):
    seqs = []
    for i in range(len(c) - 1):
        seqs.append(c[:i] + c[i+1:])
    seqs.append(c[:-1])
    return seqs



num_safe = 0
num_safe2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        c = [int(x) for x in line.split()]
        if valid_seq(c):
            num_safe += 1
        #elif valid_seq2(c):
        #    num_safe2 += 1
        else:
            for seq in subseq(c):
                if valid_seq(seq):
                    num_safe2 += 1
                    break

# Part 1
print(num_safe)

# Part 2
print(num_safe + num_safe2)
