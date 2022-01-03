# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 00:56:59 2022

@author: SamaSamrin
"""

def isPalindrome(x):
        x = str(x)
        
        #separate codes for odd length and even length
        if len(x)%2!=0:
            half = int(len(x)/2)
            if x[0:half+1]==x[half:][::-1]:
                return True
            else:
                return False
        else:
            half = int(len(x)/2)
            if x[0:half]==x[half:][::-1]:
                return True
            else:
                return False
        
        

print(isPalindrome(-12321)) #False
print(isPalindrome(12321)) #True
print(isPalindrome(13321)) #False