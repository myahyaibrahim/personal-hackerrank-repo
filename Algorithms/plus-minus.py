# Link: https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

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
    result = [0 for i in range(3)]
    positive_counter = 0
    negative_counter = 0
    netral_counter = 0
    for i in range(len(arr)):
        if (arr[i] > 0):
            positive_counter += 1
        elif (arr[i] < 0):
            negative_counter += 1
        elif (arr[i] == 0):
            netral_counter += 1

    result[0] = positive_counter/len(arr)
    result[1] = negative_counter/len(arr)
    result[2] = netral_counter/len(arr)

    print(f'{result[0]:.6f}')
    print(f'{result[1]:.6f}')
    print(f'{result[2]:.6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
