#!/usr/bin/env

class Solution:
    def medianOfSortedArrays(self, s1, s2):
        s1.extend(s2)
        s1 = sorted(s1)
        print(s1)
        
        if len(s1)%2 != 0:
            return s1[int(len(s1)/2)]
        else:
            mid_index = len(s1)//2
            print(mid_index)
            print(s1[mid_index-1])
            print(s1[mid_index])
            return ((s1[mid_index-1]+s1[mid_index])/2)
        
        

    def optimized(self, s1, s2):
        

def main():
    obj = Solution()
    print(obj.medianOfSortedArrays([], [2]))


if __name__ == '__main__':
    main()