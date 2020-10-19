def divideIntegers(dividend, divisor):
    INT_MIN = -2**31
    INT_MAX = 2**31-1
    if dividend == INT_MIN and divisor == -1: return INT_MAX
    if dividend == INT_MIN and divisor == 1: return INT_MAX

    negative = False
    if dividend < 0 and divisor < 0:
        negative = False
    elif dividend < 0 or divisor < 0:
        negative = True
    
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0

    while(dividend - divisor >= 0):
        x = 0
        print(dividend, divisor)
        while(dividend - (divisor << 1 << x) >= 0):
            print(x)
            x += 1
        quotient += 1 << x
        print(quotient)
        dividend -= divisor << x

    if negative:
        return -quotient
    else:
        return quotient




print(divideIntegers(-2147483648,1))