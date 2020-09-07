#! /usr/bin/env python3
import sys
class Solution:

    def reverseInt(self, num):
        
        negative = False
        if num < 0:
            negative = True
            num *= -1
        
        reversed = 0
        while(num > 0):
            lastdig = int(num % 10)
            reversed = (reversed * 10) +  lastdig
            num = int(num/10)
        
        if negative:
            reversed *= -1
        return reversed





def main():
    obj = Solution()
    num = 134123
    print(obj.reverseInt(num))


if __name__ == '__main__':
    main()