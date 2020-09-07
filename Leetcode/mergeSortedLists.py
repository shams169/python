#!/usr/bin/env python3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeSortedLists(self, l1, l2):
        
        temp = ListNode()
        out = []

        head = ListNode(0)
        ptr = head
        
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                ptr.next = l2
                break
            elif l2 is None:
                ptr.next = l1
                break
            else:
                lesserVal = 0
                if l1.val < l2.val:
                    lesserVal = l1.val
                    l1 = l1.next
                else:
                    lesserVal = l2.val
                    l2 = l2.next
                
                temp = ListNode(lesserVal)
                ptr.next = temp
                ptr = ptr.next
        
        return head.next


def main():
    obj = Solution()

    L1 = [1,2,3]
    L2 = [1,3,4]

    print(obj.mergeSortedLists(L1, L2))

    


 
if __name__ == '__main__':
    main()