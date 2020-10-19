def inPlaceMerge(A, B):

    result = []
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        elif A[i] > B[j]:
            result.append(B[j])
            j += 1
    
    if i < len(A):
        result.extend(A[i:])
    
    if j < len(B):
        result.extend(B[j:])
    return result


A = [1, 4, 7, 8, 10]
B = [2, 3, 9  ]
print(inPlaceMerge(A, B))