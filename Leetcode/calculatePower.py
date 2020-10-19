def calculatePower(x, y):

    if y < 0:
        negative = True
        y = abs(y)

    if y == 0:
        return 1
    elif y == 1:
        if negative:
            return 1/x
        else:
            return x
    result = x
    
    while(y > 1):
        result *= x
        y -= 1

    print(result)
    if negative:
        return 1/result
    else:
        return result


print(calculatePower(8.95371, -1))