#...................................................Count Inversions...............................................
# we have an array and we have to count the number of inversions which are countable only if
# arr[i]>arr[j] && i<j    





from sys import stdin
def getInversions(arr, n) :
    count=0
    for i in range(n):
        for j in range(1,n):
            if arr[i]>arr[j] and i<j:
                # arr[i],arr[j]=arr[j],arr[i]
                count=count+1
    return count

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))






#........................................................OPTIMAL...........................................................
# from os import *
# from sys import *
# from collections import *
# from math import *

# def getInversions(a, n) :
#     cnt = 0
#     for i in range(n):
#         for j in range(i+1, n):              #here in for loop of j we started from i+1, as we had to check that i<j for the inversion to be possible.
#             if a[i] > a[j]:                  #so we added that condition to the loop itself, making the complexity better
#                 cnt += 1
#     return cnt

# # Taking inpit using fast I/O.
# def takeInput() :
#     n = int(input())
#     arr = list(map(int, stdin.readline().strip().split(" ")))
#     return arr, n

# # Main.
# arr, n = takeInput()
# print(getInversions(arr, n))