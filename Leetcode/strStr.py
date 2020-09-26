#!/usr/bin/env python3


class Solution(object):
    def strStr(self, haystack, needle):
        if needle== "":
            return 0
        out = [i for i in range(len(haystack)) if haystack[i:len(needle)+i] == needle]
        
        if not out:
            return -1
        else:
            return out[0]

    def improved(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
def main():
    obj = Solution()
    print(obj.improved(haystack="hellower", needle= "owe"))

 
if __name__ == '__main__':
    main()
