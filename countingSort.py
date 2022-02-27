#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    array = [0]*len(arr)
    print("arr - "+str(arr))
    print("len(arr) - "+str(len(arr)))
    for x in arr:
        array[x] += 1
    return array[:100]
       
if __name__ == '__main__':
    fptr = open("countingSort.txt", 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print("result - "+str(result))

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
