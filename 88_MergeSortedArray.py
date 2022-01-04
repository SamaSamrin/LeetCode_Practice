# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:15:37 2022

@author: SamaSamrin
"""


def merge(nums1, m, nums2, n):
       
    print("length of nums1:",len(nums1))
    
    while m<len(nums1):
        print("m=", m)
        nums1[m] = nums2[len(nums1)-(m+n)]
        m+=1
            
    nums1.sort()
    
    return nums1
    
x = merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3)
print(x)

"""
merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3)
Expected: [-1,0,0,1,2,2,3,3,3]
"""