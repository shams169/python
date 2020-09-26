import itertools


def combinationSum(nums, target):

    print(itertools.combinations(nums, 1))
    print(itertools.combinations(nums, 2))


combinationSum([1,2,3,7, 9, 10], 7)