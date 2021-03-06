#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr, players):
    # Write your code here
    count = 0
    maxNum = 0
    for i in arr:
        if i > maxNum:
            maxNum = i
            count += 1
    return players[str(count % 2)]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())
    players = {"1": "BOB", "0": "ANDY"}
    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr, players)

        fptr.write(result + '\n')

    fptr.close()
