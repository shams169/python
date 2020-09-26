#!/usr/bin/env python3


class Solution():
    def moveZeros(self, nums):

        i = 0
        j = 0

        while(j < len(nums)):
            if nums[j] != 0 or nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                print(nums)
            elif nums[i] == 0 and nums[j] == 0:
                print(nums)
                j += 1
        return nums  
    

def main():
    obj = Solution()
    print(obj.moveZeros([1,0]))


if __name__ == '__main__':
    main()