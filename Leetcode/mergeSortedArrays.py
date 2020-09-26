#!/usr/bin/env python3

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


class Solution(object):
    def mergeSortedArrays(self, nums1, m, nums2, n):
        
        if n == 0:
            return
        count = m+n-1
        i = m-1
        j = n-1
        
        while(i >=0 and j >=0 ):
            if nums1[i] > nums2[j]:
                nums1[count] = nums1[i]
                count = count -1
                m = m-1
            else:
                nums1[count] = nums2[j]
                count = count -1
                j = j -1
            
            while(n >= 0):
                nums1[count] = nums2[j]
                count = count -1
                j = j - 1
        print(nums1)

    def merge(self, nums1, m, nums2, n):
        index = m + n -1
        i = m - 1
        j = n - 1

        while(index >= 0):
            if i < 0:
                nums1[index] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[index] = nums1[i]
                i -= 1
            else:
                if nums1[i] < nums2[j]:
                    nums1[index] = nums2[j]
                    j -= 1
                else:
                    nums1[index] = nums1[i]
                    i -= 1
            index -= 1
        print(nums1)
            
        


        
        

def main():

    obj = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    #nums1 = [-1,0,0,3,3,3,0,0,0]
    #nums2 = [1,2,2]
    #nums1 = [2, 0]
    #nums2 = [1]

    #obj.mergeSortedArrays(nums1, 1, nums2, 1)
    obj.merge(nums1, 3, nums2, 3)


 
if __name__ == '__main__':
    main()
