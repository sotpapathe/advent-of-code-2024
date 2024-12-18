#!/usr/bin/env python3
import sys

def number_occurrences(letters, i, j):
   
    def check(letter, i, j, incr_x, incr_y)->bool:
        built_str = "X"

        for iter in range(1, 4):
            x = i + incr_x * iter
            y = j + incr_y * iter

            if x >= 0 and x < len(letter) and y >=0 and y < len(letter[x]):
                built_str += letter[x][y]

        return built_str == "XMAS"
    
    counter = 0
    for incr_x in [-1, 0, 1]:
        for incr_y in [-1, 0, 1]:
            if incr_x == 0 and incr_y == 0:
                continue
            elif check(letters, i, j, incr_x, incr_y):
                counter += 1
    
    return counter


def number_occurrences_cross(letters, i, j):
   
    def check_pair(letter, i, j, incr_x, incr_y)->bool:
        built_str = ""

        for iter in [1, -1]:
            x = i + incr_x * iter
            y = j + incr_y * iter

            if x >= 0 and x < len(letter) and y >=0 and y < len(letter[x]):
                built_str += letter[x][y]

        return built_str == "MS" or built_str == "SM"
    
    return check_pair(letters, i, j, 1, 1) and check_pair(letters, i, j, -1, 1)
        

with open(sys.argv[1]) as f:
    letters = [x.strip() for x in f.readlines()]

counter = 0
for i in range(len(letters)):
    for j in range(len(letters[i])):
        if letters[i][j] == 'X':
            counter += number_occurrences(letters, i, j)

print(counter)

counter = 0
for i in range(len(letters)):
    for j in range(len(letters[i])):
        if letters[i][j] == 'A':
            counter += number_occurrences_cross(letters, i, j)

print(counter)
