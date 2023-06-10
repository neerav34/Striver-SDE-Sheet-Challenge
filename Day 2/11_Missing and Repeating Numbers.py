#....................................................Missing and repeating numbers....................................
# in this we are given an array and we have to find which numner is repeating and which is missing
# array contains continuous numbers starting from 1 in optimal condition(i.e. there are no repitition)




# from math import *
# from collections import *
# from sys import *
# from os import *


def missingAndRepeating(arr, n):
    arr.sort()
    a=[]
    s=0
    for i in arr:
        if i not in a:
            a.append(i)
        else:
            s=i
            if s!=0:
                break
    if arr[0]!=1:
        return[1,s]
    for i in range(1,n+1):
        if i not in arr:
            return[i,s]
        


    
arr = [1,2,2,3,4,5,6]
s = missingAndRepeating(arr, 7)
print(s)
