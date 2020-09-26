#!/usr/bin/env python3


class Solution:
    def removeElement(self, nums, val):

        i = 0
        j = len(nums)
        while(i < j):

            if nums[i] == val:
                nums.pop(i)
                j -= 1
            else:
                i += 1
        return len(nums)


def main():
    obj = Solution()
    print(obj.removeElement([2,3,4,5,3,6,3], 3))


if __name__ == '__main__':
    main()

































# class Solution(object):
#     def removeElement(self, nums, val):
        
#         i = len(nums)
#         j = 0

#         while(j < i):
#             if nums[j] == val:
#                 nums.pop(j)
#                 i = i-1
#             else:
#                 j = j+1
        
#         print(nums)
   
# def main():
#     obj = Solution()
#     nums = [1,2,2,3,4]
#     val = 2
#     obj.removeElement(nums, val)

 
# if __name__ == '__main__':
#     main()
