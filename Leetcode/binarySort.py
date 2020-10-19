def binarySort(nums):
    i = 0
    j = 0

    if len(nums) <= 1:
        return nums

    while(j < len(nums)):
        if nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            i += 1
        else:
            j += 1

    return nums


def main():
    print(binarySort([0,1,1,0,0,1,0,1,0,0]))


if __name__ == '__main__':
    main()

