def findDuplicate(A):

    n = len(A)

    for i in range(len(A)):
        val = abs(A[i])
        curr = A[val]
        if A[val] < 0 :
            return val
        else:
            A[val] = -A[val]

print(findDuplicate([1, 2, 3, 4, 2]))