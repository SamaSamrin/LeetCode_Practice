# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 01:23:53 2022

@author: SamaSamrin
"""

def bitwiseComplement(n):
        binary_of_n = str(format(n, "b"))
        print(binary_of_n)
        complement_of_n = ''
        for i in binary_of_n:
            if i=="0":
                complement_of_n = complement_of_n + "1"
            elif i=="1":
                complement_of_n = complement_of_n + "0"
        print(complement_of_n)
        final_int = int(complement_of_n,2)
        print(final_int)
        return final_int
        
print(bitwiseComplement(10)) #answer = 5
print(bitwiseComplement(5)) #answer = 2
print(bitwiseComplement(7)) #answer = 0