def checkPhoneNumUnique(A):

    A = list(A)
    print(A)

    for i in range(len(A)):
        print(A[A[i]])
        if A[A[i-1]] == -1:
            return "Not Unique" 
        else:
            A[i] = -1
    print('Unique')


print(checkPhoneNumUnique([1,2,3,3,4,5,6,7,8]))