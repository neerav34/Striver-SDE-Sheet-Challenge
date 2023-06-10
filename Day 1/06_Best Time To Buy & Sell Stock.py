#..............................best time to buy and sell stocks....................................


from os import *# type: ignore  
from sys import *# type: ignore  
from collections import *# type: ignore  
from math import *# type: ignore  

def maximumProfit(prices):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(prices)):
        minPrice = min(minPrice, prices[i])
        maxPro = max(maxPro, prices[i] - minPrice)
    return maxPro






#...........................................brute force approach................................

# from typing import List

# def maxProfit(arr: List[int]) -> int:
#     maxPro = 0
#     n = len(arr)


#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[j] > arr[i]:
#                 maxPro = max(arr[j] - arr[i], maxPro)


#     return maxPro


# if __name__ == "__main__":
#     arr = [7, 1, 5, 3, 6, 4]
#     maxPro = maxProfit(arr)
#     print("Max profit is: ", maxPro)
