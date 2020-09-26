#!/usr/bin/env python3

def twoSum(nums, target):

    i = 0
    j = len(nums) - 1

    while(i < j):
        if nums[i] + nums[j] == target:
            return [i+1, j+1]
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1

    return None


print(twoSum([2,7,11, 15], 9))
print(twoSum([-3,2,3,3,6,8,15], 9))