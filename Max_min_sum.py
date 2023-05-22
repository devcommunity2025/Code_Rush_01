
'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    maxi=max(arr)
    mini=min(arr)
    arr_sum=sum(arr)
    min_sum= arr_sum-maxi
    max_sum=arr_sum-mini
    print(min_sum,max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

