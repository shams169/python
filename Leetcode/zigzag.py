#!/usr/bin/env python3


class Solution:

    def convertIntoZigzag(self, s, nnumRows):

        direction = -1
        if numRows == 1:
            return s
        result = [[] for i in range(numRows)]
        row = 0
        for c in s:
            result[row].append(c)

            if row == 0 or row == numRows-1:
                direction *= -1
            
            row += direction
        
        print(''.join([''.join(x) for x in result]))
        


def main():
    obj = Solution()
    obj.convertIntoZigzag('AB', 1)

if __name__ == "__main__":
    main()