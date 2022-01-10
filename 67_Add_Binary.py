"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Example 3:
Input: a = "11111", b = "11111"
Output: "111110"

"""

def addBinary(a, b):
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]
    
 """
 Explanation: We first convert the string a into a binary with int(a, 2), where the second argument denotes the base.
 Then the bin() function converts and returns the binary equivalent string of their resulting sum
 Since this results in the sum string having a prefix of "0b", we deduct it while returning by eliminating the first two characters of sum.
 """
