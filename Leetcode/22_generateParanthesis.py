def helper(res, currStr, nOpen, nClose, n):
    if len(currStr) == n*2:
        res.append(currStr)
        return
    if (nOpen < n):
        helper(res, currStr+"(", nOpen+1, nClose, n)

    if (nClose < nOpen):
        helper(res, currStr+")", nOpen, nClose+1, n)



def generateParanthesis(n):
    result = []

    helper(result, "", 0, 0, n)
    return result
    
    pass





print(generateParanthesis(3))