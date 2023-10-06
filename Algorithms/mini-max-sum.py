# Link: https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    current_sum = 0
    for i in range(len(arr)-1):
        current_sum = current_sum + arr[i]
    current_mini = current_sum
    current_max = current_sum

    for i in range(len(arr)):
        current_sum = 0
        for j in range(len(arr)):
            if (j != i):
                current_sum = current_sum + arr[j]
        if (current_sum < current_mini):
            current_mini = current_sum
        elif (current_sum > current_max):
            current_max = current_sum

    print(str(current_mini)+' '+str(current_max))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
