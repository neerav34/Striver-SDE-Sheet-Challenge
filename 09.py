#.........................................Merge Sorted Arrays...........................................
# we are given 2 arrays we have to merge them and then sort them...also there should be no 0's in the final array





from math import *  # type:ignore
from collections import *  # type:ignore
from sys import *  # type:ignore
from os import *  # type:ignore


def ninjaAndSortedArrays(arr1, arr2, m, n):
    left = m - 1
    right = 0
    for i in range(len(arr1)):
        if 0 in arr1:
            arr1.remove(0)
    # Swap the elements until arr1[left] is smaller than arr2[right]:
    while left >= 0 and right < n:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    arr1.sort()
    arr2.sort()

    arr1 = arr1 + arr2
    return arr1

    
