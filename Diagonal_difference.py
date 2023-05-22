'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:
    1 2 3
    4 5 6
    9 8 9 
The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 3+5+9=17.
 Their absolute difference is |15-17|=2
'''
#code

#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    left_diag=0
    right_diag=0
    for i in range(len(arr)):
        # add when both row and columns are same
        left_diag+=arr[i][i] 
        # make mathematical eqn to find column index of right diagonal
        k=(n-1)-i
        right_diag+=arr[i][k]
    diag_diff=abs(left_diag-right_diag)
    return diag_diff
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
