#................................ Set matrix zeroes ...................................................



# set respective rows and columns to zeroes which have matrix[r][c]==0


from math import * # type: ignore
from collections import * # type: ignore
from sys import * # type: ignore
from os import * # type: ignore

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    ROWS,COLS= len(matrix),len(matrix[0])
    rowZero = False
    for r in range(ROWS): 
        for c in range(COLS): 
            if matrix[r][c] == 0:
 
                matrix[0][c] = 0 
                if r > 0:

                    matrix[r][0]= 0

                else:

                    rowZero = True

    for r in range(1, ROWS):

        for c in range(1, COLS):

            if matrix[0][c]== 0 or matrix[r][0]==0:
                 matrix[r][c]=0

    if matrix[0][0] == 0:

        for r in range(ROWS): 
            matrix[r][0] = 0

    if rowZero:
        for c in range (COLS): 
            matrix[0][c]=0
    
    
