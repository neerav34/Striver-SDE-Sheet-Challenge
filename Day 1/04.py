#.......................................MAXIMUM SUBARRAY SUM.............................................
# return the maximum sum of elements among all the subarrays (continuous subarrays) of a given array

from os import * # type: ignore
from sys import *# type: ignore
from collections import *# type: ignore
from math import *# type: ignore
import sys

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
# list=[]
def maxSubarraySum(arr, n) :
    maxi = -sys.maxsize-1
    sum = 0

    for i in range(n):
        sum += arr[i]

        if sum > maxi:
            maxi = sum


        if sum < 0:
            sum = 0
    if maxi < 0: maxi = 0
    return maxi

