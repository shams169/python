def sumPairArray(nums, target):
    nums_map = {}

    for i in range(len(nums)):
        comp = target - nums[i]

        if comp in nums_map:
            return [nums_map[comp], i]
        nums_map[nums[i]] = i

    return "Pair not found"

def main():
    print(sumPairArray([8,7,2,5,3,1], 10))


if __name__ == '__main__':
    main()



