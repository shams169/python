#!/usr/bin/env python3
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next




class Solution(object):
    def mergeSortedLists(self, L1, L2):
        print(L1)
        print(L2)
        print(L1.extend(L2))


def main():
    obj = Solution()

    L1 = [1,2,3]
    L2 = [1,3,4]

    print(obj.mergeSortedLists(L1, L2))

    


 
if __name__ == '__main__':
    main()