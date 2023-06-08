# ...........................................Sort 1 2 3...............................................................



# takes first input : how many arrays
# second line input : no. of elements in the array
# returns the array in ascending order
# example:
# 2              (inputs)
# 4
# 3 2 4 0
# 5
# 3 6 2 3 0
# 0 2 3 4        (outputs)
# 0 2 3 3 6


from os import *  # type: ignore      ....................................  # remove yellow errors....................................................
from sys import * # type: ignore
from collections import * # type: ignore
from math import * # type: ignore

from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


def sort012(arr, n):
    arr.sort()
    # write your code here
    # don't return anything
    pass


# taking inpit using fast I/O
def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


def printAnswer(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main

t = int(input().strip())
for i in range(t):
    arr, n = takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
