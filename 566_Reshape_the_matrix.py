# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 19:22:38 2022

@author: SamaSamrin

Runtime: 183 ms
Memory Usage: 26 MB
"""

import numpy as np

def matrixReshape(mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    mat = np.array(mat)
    try:
        new_array = mat.reshape(r,c)
        return new_array
    except Exception:
        return mat

print(matrixReshape([[1,2],[3,4]], 1, 4)) #returns new array
print(matrixReshape([[1,2,3],[4,5,6]], 3, 2)) #returns new array
print(matrixReshape([[1,2],[3,4]], 2, 4)) #returns old array