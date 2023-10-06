# Link: https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    # Write your code here
    index = 1
    while (index <= n):
        for i in range(n-index):
            print(' ', end='')
        for i in range(index):
            print('#', end='')
        print("")
        index += 1


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
