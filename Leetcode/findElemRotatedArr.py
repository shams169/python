"""
Search an element in a sorted rotated array
"""

def findPivot(A, low, high):
    
    if low > high:
        return
    mid = (low + high) // 2

    if mid < high and A[mid] > A[mid+1]:
        return mid
    if mid > low and A[mid] < A[mid-1]:
        return mid-1
    if A[0] >= A[mid]:
        return findPivot(A, low, mid-1)
    return findPivot(A, mid+1, high)

def searchBinary(A, low, high, key):

    if low > high:
        return -1
    
    mid = (low + high) // 2

    if A[mid] == key:
        return mid
    if A[mid] > key:
        return searchBinary(A, low, mid-1, key)
    return searchBinary(A, mid+1, high, key)



def findElementRotatedArray(A, target):

    pivot = findPivot(A, 0, len(A)-1)
    print(pivot)
    # If we dint find the pivot, the array is not rotated at all
    if pivot == -1:
        searchBinary(A, 0, len(A)-1, target)
    
    if A[pivot] == target:
        return pivot
    
    if A[0] <= target:
        return searchBinary(A, 0, pivot-1, target)
    return searchBinary(A, pivot+1, len(A)-1, target)
    


print(findElementRotatedArray([4, 5, 6, 7, 8, 9, 1, 2, 3], 5))
print(findElementRotatedArray([7, 8, 9, 1, 2, 3, 4, 5, 6], 5))






# def findPivot(A, low, high):

#     if high < low:
#         return -1
#     if high == low:
#         return low
    
#     mid = (low+high) // 2

#     if mid < high and A[mid] > A[mid+1]:
#         return mid
#     if mid > low and A[mid] < A[mid-1]:
#         return mid-1
#     if A[low] >= A[mid]:
#         return findPivot(A, low, mid-1)
#     return findPivot(A, mid+1, high)

# def binarySearch(A, low, high, key):

#     if low > high:
#         return -1
    
#     mid = (low + high) // 2

#     if A[mid] == key:
#         return mid
    
#     if key > A[mid]:
#         return binarySearch(A, mid+1, high, key)
#     return binarySearch(A, low, mid-1, key)

# def findElemRotatedArray(A, target):

#     pivot = findPivot(A, 0, len(A)-1)
    
#     index = binarySearch(A, 0, len(A)-1, target)
#     print(index)


# print(findElemRotatedArray([4, 5, 6, 7, 8, 9, 1, 2, 3], 5))

