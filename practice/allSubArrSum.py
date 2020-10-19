from collections import defaultdict

def allSubArraysSum(A, target):

    sum_map = {}
    sum_map.setdefault(0, []).append(-1)

    currSum = 0
    result = []

    for i in range(len(A)):
        currSum += A[i]
        diff = currSum - target
        if diff in sum_map:
            olist = sum_map.get(diff)
            for item in olist:
                result.append(A[item+1: i+1])
        sum_map.setdefault(currSum, []).append(i)

    return result

print(allSubArraysSum([3, 4, -7, 3, 1, 3, 1, -4, -2, -2 ], 0))
