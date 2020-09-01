#!/usr/bin/env python3

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return  [i,j]
        return []

    def eff_twoSum(self, nums, target):
        print('xxx')
        values_dict = {}
        
        for i, val in enumerate(nums):
            print(values_dict)
            comp = target - val
            print(comp)
            if comp in values_dict.keys():
                return [values_dict[comp], i]
            values_dict[val] = i
            print('-----------------------------')
        return []

def main():
    nums = [3,2,4]
    target = 5
    obj = Solution()
    out = obj.eff_twoSum(nums, target)
    print(out)


if __name__ == '__main__':
    main()




