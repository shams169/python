import os

def sockMerchant(n, ar):
    out = {}
    for i in ar:
        if i in out:
            out[i] += 1
        else:
            out[i] = 1
    
    count = 0
    print(out)
    for val in out.values():
        if val >= 2:
            count += val//2
    return int(count)

if __name__ == '__main__':
    fptr = open('./out', 'w')

    n = int(input())
    print(n)

    ar = list(map(int, input().rstrip().split()))
    print(ar)

    result = sockMerchant(n, ar)
    print('Result: {}'.format(result))

    #fptr.write(str(result) + '\n')

    #fptr.close()