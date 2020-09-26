#!/usr/bin/env python3

class Solution(object):
    def isPalindrome(self, x):

        out = []
        input = x
        temp = 0
        while(x > 0):
            mod = x%10
            temp = temp*10 + mod 
            x = x//10
        print(temp)
        if input == temp:
            return True
        else:
            return False

        
        
        




def main():
    obj = Solution()
    x = 1214
    print(obj.isPalindrome(x))

 
if __name__ == '__main__':
    main()