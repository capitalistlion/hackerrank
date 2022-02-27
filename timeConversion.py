#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    h = int(s[:2])
    msec = s[2:8]
    h = h % 12 if s[-2:] == "AM" else h % 12 + 12
    return f"{h:02}{msec}"

if __name__ == '__main__':
    fptr = open("file.txt", 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
