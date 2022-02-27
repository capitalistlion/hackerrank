#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    posNum = len(list(filter(lambda a: a > 0, arr)))
    negNum = len(list(filter(lambda a: a < 0, arr)))
    arrayLen = len(arr)
    zeroNum = arrayLen - (posNum + negNum)
    print(format(round(posNum/arrayLen, 6), '.6f'))
    print(format(round(negNum/arrayLen, 6), '.6f'))
    print(format(round(zeroNum/arrayLen, 6), '.6f'))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
