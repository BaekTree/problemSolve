# https://www.hackerrank.com/challenges/one-month-preparation-kit-angry-children/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr = sorted(arr)

    # Problem redefinition: Find the smallest range
    # with the window size k, move from 0 to n - k.
    # get the minimum of max - min.
    # var: min_distance
    # index i = 0 to n - k
    # e.g k = 4,
    # e.g. (0,1,2,3)
    # e.g. if n = 7, (3,4,5,6). 
    # gen: from [ i to i + k - 1 ].
    # loop end condition: if i + k - 1 == n, end loop.
    min_distance = float('inf')
    for i in range(len(arr)):
        if i + k - 1 == len(arr):
            break
        min_distance = min(min_distance, arr[i + k - 1] - arr[i])
    return min_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
