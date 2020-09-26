"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
Solution from here: https://dev.to/13point5/maximum-subarray-3c5l
"""

class Solution:
    def maxSubArray(self, nums):
        ans = nums[0]
        subarray_sum = nums[0]
        
        for i in range(1, len(nums)):
            subarray_sum = max(nums[i], nums[i]+subarray_sum)
            ans = max(ans, subarray_sum)
          
        return(ans)
            
        
    

def main():
    obj = Solution()
    print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == '__main__':
    main()