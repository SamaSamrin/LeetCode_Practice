# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:26:33 2022

@author: ASUS
"""

def containsDuplicate(nums):
        print(set(nums))
        if len(nums)==len(set(nums)):
            return True
        else:
            return False
        
print(containsDuplicate([1,2,3,1]))
