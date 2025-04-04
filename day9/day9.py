#!/usr/bin/env python3
import sys

def expand(disk_map):
    id = 0
    blocks = []
    for i, c in enumerate(disk_map):
        if i % 2 == 0:
            for j in range(int(c)):
                blocks.append(id)
            id += 1
        else:
            for j in range(int(c)):
                blocks.append(-1)
    return blocks

def pack(blocks):
    idx_start = blocks.index(-1)
    idx_end = len(blocks) - 1
    while idx_start < idx_end:
        while blocks[idx_end] < 0:
            idx_end -= 1
        blocks[idx_start] = blocks[idx_end]
        blocks[idx_end] = -1
        idx_start = blocks.index(-1, idx_start + 1)

def pack2(blocks):
    def file_found(files, file_id, file_idx, file_size):
        files[file_id] = [(file_idx, file_size)]

    def free_found(free_space, free_idx, free_size):
        if free_size in free_space:
            free_space[free_size].append(free_idx)
        else:
            free_space[free_size] = [free_idx]

    free_space = {}
    files = {}
    free_size = 0
    file_size = 0
    file_id = 0
    for i, id in enumerate(blocks):
        if id == -1:
            free_size += 1
            if file_size > 0:
                file_found(files, file_id, i - file_size, file_size)
                file_size = 0
        else:
            if id != file_id:
                file_found(files, file_id, i - file_size, file_size)
                file_size = 0
            file_id = id
            file_size += 1
            if free_size > 0:
                free_found(free_space, i - free_size, free_size)
                free_size = 0
    if file_size > 0:
        file_found(files, file_id, len(blocks) - file_size, file_size)
    if free_size > 0:
        free_found(free_space, len(blocks) - 1 - free_size, free_size)
    for id in reversed(files.keys()):
        print(id)

def checksum(blocks):
    s = 0
    for i, id in enumerate(blocks):
        if id < 0:
            break
        s += i * id
    return s

def pretty_str(blocks):
    def num2char(x):
        if x < 0:
            return '.'
        else:
            return str(x)
    return ''.join([num2char(x) for x in blocks])



with open(sys.argv[1]) as f:
    disk_map = f.readline().strip()
blocks = expand(disk_map)
blocks2 = [x for x in blocks]
print(pretty_str(blocks))
pack(blocks)
pack2(blocks2)
print(checksum(blocks))
print(checksum(blocks2))
