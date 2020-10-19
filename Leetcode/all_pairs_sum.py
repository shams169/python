def findAllPairsSum(nums, target):
    nums_map = {}
    result_list = []
    

    for i in range(len(nums)):
        comp = int(target - nums[i])
        if  comp in nums_map:
            print(nums_map[comp], i)
        else:
            nums_map[nums[i]] = i


print(findAllPairsSum([0, 14, 4, 7, 8, 3, 5, 7], 11))
print(findAllPairsSum([8, 7, 2, 5, 3, 1], 10))