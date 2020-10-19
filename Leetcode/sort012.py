def sortThreewayPartition(A):

    start = 0
    mid = 0
    pivot = 1
    end = len(A) -1

    while(mid <= end):
        if A[mid] < pivot:
            A[mid], A[start] = A[start], A[mid]
            mid += 1
            start += 1
        elif A[mid] > pivot:
            A[mid], A[end] = A[end], A[mid]
            end -= 1
        else:
            mid += 1
    return A

A = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
print(sortThreewayPartition(A))

