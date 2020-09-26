#!/usr/bin/env python3

class Solution:
    def bruteForce(self, head)
        temp = head
        count = 0
        mid = 0
        while temp is not None:
            count += 1
            temp = temp.next
        
        print(count)  
        if count % 2 == 0:
            mid = (count // 2) + 1
        else:
            mid = int(count / 2 ) + 1
        
        temp2 = head
        
        for i in range(0, mid-1):
            temp2 = temp2.next
            
        head = temp2
        return temp2

    def middleNode(self, head)

        i = j = head

        while(j is not None and j.next is not None):
            i = i.next
            j = j.next.next
        
        return i