#https://www.hackerrank.com/challenges/one-month-preparation-kit-bomber-man/problem?h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


def bomb(b,r,c):
    field = [['O' for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            if b[i][j] == 'O':
                field[i][j] = '.'
                if i+1<r:
                    field[i+1][j] = '.'
                if i>0:
                    field[i-1][j] = '.'
                if j+1<c:
                    field[i][j+1] = '.'
                if j>0:
                    field[i][j-1] = '.'
    return field

def bomberMan(n, grid):
    
    # Write your code here
    r = len(grid)
    c = len(grid[0])
    if n < 2:
        # print("N<2")
        return grid
    elif n % 2== 0:
        # print("N%2 == 0")
        grid = [['O' for i in range(c)] for j in range(r)]
        for i in range(r):
            grid[i] = "".join(grid[i])
        return grid
    else:
        if (n + 1) % 4 == 0:
            # print("n + 1 % 4 == 0")
            grid = bomb(grid, r, c)
        elif (n - 1) % 4 == 0:
            # print("n - 1 % 4 == 0")
            grid = (bomb(bomb(grid, r, c), r ,c))
        # else:
            # print(n)
    for i in range(r):
        grid[i] = "".join(grid[i])
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
