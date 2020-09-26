#!/usr/bin/env python3


class Solution:
    def reverseString(self, s):

        i = 0
        j = len(s) - 1

        while(i < j):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return s

def main():
    obj = Solution()

    print(obj.reverseString(["H","a","n","n","a","h"]))


if __name__ == '__main__':
    main()