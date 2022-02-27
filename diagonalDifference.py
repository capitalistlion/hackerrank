#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diag1 = diag2 = 0
    maxLen = max([len(i) for i in arr])
    diag1 = sum([arr[count][count] for count in range(len(arr)) if len(arr[count]) == maxLen])
    diag2 = sum([arr[count][len(arr[count])-1-count] for count in range(len(arr)) if len(arr[count]) == maxLen])
    return abs(diag1-diag2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
