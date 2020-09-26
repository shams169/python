#!/usr/bin/env python3


class Solution:
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        
        if len(nums) == 0:
            return len(nums)
        
        while(j < len(nums)):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
        print(nums)
        return len(nums)

def main():
    obj = Solution()
    print(obj.removeDuplicates([1,1,1,2,3,4,5,5,6,6]))


if __name__ == '__main__':
    main()