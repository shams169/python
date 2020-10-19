def printmatrix(mat):
    for row in mat:
        print(row)

def regexMatch(t, p):
    rows = len(p)+1
    cols = len(t)+1

    T = [ [0]*rows for j in range(cols)]
    T[0][0] = True
    
    for i in range(1, len(T[0])):
        print(p[i-1])
        if p[i-1] == "*":
            T[0][i] = T[0][i-2]
            printmatrix(T)
    

    for x in range(1, len(t)):
        for y in range(1, len(T[0])):
            if p[y-1] == "." or p[y-1] == t[x-1]:
                T[x][y] = T[x-1][y-1]
                printmatrix(T)
            elif p[y-1] == '*':
                T[x][y] = T[x][y-2]
                if p[y-2] == '.' or p[y-2] == t[y-1]:
                    T[x][y] = T[x][y] | T[x-1][y]
                    printmatrix(T)
            else:
                T[x][y] = False
                printmatrix(T)

    return T[len(t)][len(p)]
    




print(regexMatch('xaabyc', 'xa*b.y'))
