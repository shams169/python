#!/usr/bin/env python3
"""
66. Plus One
Easy

Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:

Input: digits = [0]
Output: [1]

"""




class Solution(object):
    def plusOne(self, digits):
        
        num = 0
        for x in digits:
            num = str(num) + ''.join(str(x))
            print(num)  
        num = int(num)
        print(num)
        num += 1
        num = str(num)
        print(list(num))


    def betterSolution(self, digits):
        carry = 1
        for i in reversed(range(len(digits))):
            carry, digits[i] = divmod(digits[i]+carry, 10)

        if carry > 0:
            return [carry] + digits
        else:
            return digits



            
def main():
    obj = Solution()
    print(obj.plusOne([1,2,3]))



 
if __name__ == '__main__':
    main()
