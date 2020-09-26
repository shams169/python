#!/usr/bin/env python3
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

NOTE: There is an important observation to be made here:

if n = 1 (1) -- [1]
if n = 2 (2) -- [1, 1], [2]
if n = 3 (3) -- [1,1,1,], [1, 2], [2, 1]
if n = 4 (5) -- [1,1,1,1], [1,2,1], [1,1,2], [2,1,1], [2,2]
if n = 5 ()  -- [1,1,1,1,1], [1,1,1,2], [1,1,2,1] [1,2,1,1], [2,1,1,1], [2,1,2], [1,2,2], [2,2,1], 
"""


class Solution:
    def climbStairs(self, n):
        a = 1
        b = 2
        result = 0
        if n == 1:
            return a 
        elif n == 2:
            return b
        else:
            for i in range(3, n+1):
                result = a+b
                a = b
                b = result
        return result

def main():
    obj = Solution()
    print(obj.climbStairs(38))

if __name__ == '__main__':
    main()