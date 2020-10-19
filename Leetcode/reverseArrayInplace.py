def reverseArray(nums):

    i = 0
    j = len(nums) -1

    while(i < j):
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    return nums

print(reverseArray([2,3,4,6,7,2,8]))
print(reverseArray([1,2,3,4,5,6,7]))
