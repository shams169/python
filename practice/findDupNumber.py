def findDuplicateNumber(A):
    hare = tortoise = A[0]

    while True:
        tortoise = A[tortoise]
        hare = A[A[hare]]
        if tortoise == hare:
            break
    tortoise = A[0]

    while(tortoise != hare):
        tortoise = A[tortoise]
        hare = A[hare]
    return tortoise


print(findDuplicateNumber([1, 2, 3, 3, 4]))