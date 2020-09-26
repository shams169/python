class Solution:   
    def letterCombinations(self, digits):

        if len(digits) == 0:
            return []
        
        sol = []
        self.helper(digits, '', sol)
        return sol

    
    def helper(self, digits, currStr, sol):
        if len(digits) == 0:
            sol.append(currStr)
            return
        
        possibleChars = self.digitMapping(digits[0])

        for ch in possibleChars:
            currStr += ch
            self.helper(digits[1:], currStr, sol)
            currStr = currStr[:-1]

    
    def digitMapping(self, digit):
        mapping = { '2' : 'abc',
                    '3' : 'def',
                    '4' : 'ghi',
                    '5' : 'jkl',
                    '6' : 'mno',
                    '7' : 'pqrs',
                    '8' : 'tuv',
                    '9' : 'wxyz',
                    }
        return mapping[digit]



def main():
    obj = Solution()
    print(obj.letterCombinations("233"))

if __name__ == '__main__':
    main()