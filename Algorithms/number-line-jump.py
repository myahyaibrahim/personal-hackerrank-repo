# https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def kangaroo1(x1, v1, x2, v2):
    # Write your code here
    x1Pos = x1
    x2Pos = x2
    result = "NO"
    while (True):
        if (x1Pos == x2Pos):
            result = "YES"
            break
        if (abs(x1Pos-x2Pos) < abs((x1Pos + v1)-(x2Pos + v2))):
            break
        x1Pos += v1
        x2Pos += v2
    return result


def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if (x2 > x1 and v2 > v1):
        return "NO"
    else:
        if v2-v1 == 0:
            return "NO"
        else:
            if ((x1-x2) % (v2-v1) == 0):
                return "YES"
            else:
                return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
