def iterFibo(n):

    f0 = 0
    f1 = 1

    for i in range(2, n+1):
        F = f0 + f1
        f0 = f1
        f1 = F
    return F

def recursiveFibo(n):
    if n <= 1:
        return n
    
    return recursiveFibo(n-2) + recursiveFibo(n-1)

def main():
    #print(iterFibo(40))
    print(recursiveFibo(40))
    

if __name__ == '__main__':
    main()