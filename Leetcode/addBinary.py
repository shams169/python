#!/usr/bin/env python3
"""
67. Add Binary
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution(object):
    def addBinary(self, a, b):

        i = len(a) - 1
        j = len(b) - 1
        result = []

        carry = 0
        while(i >= 0 or j >=0 ):
            sum = carry

            if i >= 0:
                sum += int(a[i])
            
            if j >= 0:
                sum += int(b[j])
            
            result.insert(0,sum%2)
            carry = int(sum/2)
            i -= 1
            j -= 1
        if carry:
            result.insert(0,1)        
        print(''.join([str(x) for x in result]))





def main():
    obj = Solution()
    print(obj.addBinary('11', '1'))

 
if __name__ == '__main__':
    main()
