class Node():
    pass

def swapNodeInPairs(self):
        d1 = d = Node(0)
        d.next= self.head

        while d.next and d.next.next:
            p = d.next
            q = d.next.next

            d.next = q
            p.next = q.next
            q.next = p

            d = p
        self.head = d1.next
        self.printNodes()