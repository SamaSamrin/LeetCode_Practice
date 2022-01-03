# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 20:58:34 2022

@author: ASUS
"""
from sys import maxint

def maxSubArray(self, nums):
        size = len(nums)
        max_so_far = -maxint - 1 #maximum subarray ending at this index
        max_ending_here = 0  #maximum subarray overall so far

        for i in range(0, size):
            max_ending_here = max_ending_here + nums[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0   
        return max_so_far

a = maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) #answer 6
print("1st Answer: ", a)

b= maxSubArray([5,4,-1,7,8]) #answer 23
print("2nd Answer: ", b)

c= maxSubArray([1]) #answer 1
print("3rd Answer: ", c)


"""
  Runtime = 596 ms
  Memory = 25.7 MB
"""
