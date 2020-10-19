def leftRightSum(A):

    totalSum = sum(A)
    half = 0
    for i in range(len(A)):
        if half == (totalSum - A[i]) // 2:
            return i
        half += A[i]
    return -1

print(leftRightSum([2,3, 4, 1, 4, 5]))
