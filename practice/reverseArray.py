def reverseArray(nums):
    
    count = len(nums)
    print(count)
    for i in range(count//2):
        nums[i], nums[count-1-i] = nums[count-1-i], nums[i]
    
    return nums

def main():
    nums1 = [1, 2, 2, 6, -1, 6, 7]
    print(reverseArray(nums1))


if __name__ == '__main__':
    main()