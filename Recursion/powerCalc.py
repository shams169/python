def powerCalc(x, n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(n):
            result = result*x
        return result

def recursivePower(x, n):
    if n == 0:
        return 1
    else:
        return x * recursivePower(x, n-1)

    

def main():
    #result = powerCalc(5, 3)
    result = recursivePower(5, 3)
    print(result)

if __name__ == '__main__':
    main()
