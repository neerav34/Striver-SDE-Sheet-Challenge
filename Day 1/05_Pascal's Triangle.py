from math import *
from collections import *
from sys import *
from os import *

def printPascal(row):
    res = [[1]]
    for i in range(row-1):
        temp = [0]+res[-1]+[0]
        r=[]
        for j in range(len(res[-1])+1):
            r.append(temp[j]+temp[j+1])
        res.append(r)
    return res
