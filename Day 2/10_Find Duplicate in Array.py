#.............................................Finding Duplicate in Array...............................................
from os import *#type:ignore
from sys import *#type:ignore
from collections import *#type:ignore
from math import *#type:ignore

def findDuplicate(arr:list, n:int):
    ans=[]
    for (i) in arr:
        if i not in ans:
            ans.append((i))
        else:
       
            return (i)
    pass




#................................................C++ solution...............................................................
#include <bits/stdc++.h>

# int findDuplicate(vector<int> &nums, int n){
# 	int slow = nums[0];
#   int fast = nums[0];
#   do {
#     slow = nums[slow];
#     fast = nums[nums[fast]];
#   } while (slow != fast);
#   fast = nums[0];
#   while (slow != fast) {
#     slow = nums[slow];
#     fast = nums[fast];
#   }
#   return slow;
# 	// Write your code here.
# }
