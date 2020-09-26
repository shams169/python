def threeSum(nums, target):

    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue

        j = i+1
        k = len(nums) -1

        while(j < k):
            temp = nums[i] + nums[j] + nums[k]

            if temp == target:
                result.append((nums[i], nums[j], nums[k]))

                while(nums[j] == nums[j+1]):
                    j += 1
                while(nums[k] == nums[k-1]):
                    k -= 1
                j += 1
                k -= 1
            elif temp < target:
                j += 1
            else:
                k -= 1
    return result

print(threeSum([-1,0,1,2,-1,-4], 0))
