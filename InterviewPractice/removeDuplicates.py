#!/usr/bin/env python3

import random

def remove_dups(input):
    out = []
    for i in input:
        if i not in out:
            out.append(i)
    return out
        
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        print('Sorted Nums: {}'.format(nums))
        a = 1
        
        while(a < len(nums)):
            if nums[a-1] == nums[a]:
                nums.pop(a)
            else:
                a = a+1
        print(nums)
        


def main():
    input = [0,1,2,1,1,2,2,4,3,3]
    sol = Solution()
    sol.removeDuplicates(input)
    #print(sol.removeDuplicates(input))

    #input = [random.randint(1,5) for i in range(10)]
    #input = ['some', 'val', 'are', 'are', 'val', 'dups', 'some', 'dups']
    #print(remove_dups(input))



if __name__ == '__main__':
    main()