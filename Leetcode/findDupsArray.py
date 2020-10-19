from collections import defaultdict

def findDuplicates(nums):

    nums_map = defaultdict(int)
    dups_set = set()
    for i, val in enumerate(nums):
        nums_map[val] += 1

        if nums_map[val] > 1:
            dups_set.add(val)

    return dups_set


"""
Find duplicates in O(n) time and O(1) extra space | Set 1
Given an array of n elements which contains elements from 0 to n-1, 
with any of these numbers appearing any number of times. 
Find these repeating numbers in O(n) and using only constant memory space.
"""

def OptimalSolution(nums):
    n = len(nums)
    dups = []
    for i in range(len(nums)):
        val = nums[abs(nums[i])]
        if val > 0:
            nums[abs(nums[i])] = -nums[abs(nums[i])]
        else:
            dups.append(abs(nums[i]))

    return dups

#print(findDuplicates([1, 2, 3, 1, 3, 6, 6]))
print(OptimalSolution([1, 2, 3, 1, 3, 6, 6]))
    