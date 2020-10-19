class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    
    def printNodes(self):

        temp = self.head
        out = []
        while(temp != None):
            out.append(temp.val)
            temp = temp.next
        print(out)


    def appendNode(self, Node):
        temp = self.head
        if not temp:
            self.head = Node
            return

        while(temp.next != None):
            temp = temp.next
        temp.next = Node
    
    def insertAt(self, i, Node):
        index = 0
        temp = self.head
        
        # Insert at the start of the linkedlist
        if i == 0:
            temp = Node
            temp.next = self.head
            self.head = temp
        else:
            while(temp.next != None):
                if i == index+1:
                    Node.next = temp.next
                    temp.next = Node
                    return
                else:
                    index += 1
                    temp = temp.next
            if index+1 == i:
                temp.next = Node
            else:
                raise IndexError



    def deleteNode(self, val):
        
        curr = self.head
        prev = self.head

        # UC1: Check if we have to delete the head node
        if curr.val == val:
            self.head = curr.next
            return
        else:
            curr = prev.next

        while(curr.next != None):
            if curr.val == val:
                prev.next = curr.next
                return
            else:
                curr = curr.next
                prev = prev.next
        if curr.val == val:
            prev.next = None

    def deleteNodeAtIndex(self, n):
        temp1 = self.head

        if n == 0:
            self.head = temp1.next
            return


        for i in range(0, n-1):
            temp1 = temp1.next
        
        print(temp1.val)
        temp2  = temp1.next
        print(temp2.val)
        temp1.next = temp2.next
        return
    

    # def reverseLinkedList(self):

    #     prev = None
    #     curr = self.head
        

    #     while(curr is not None):
    #         temp = curr.next
    #         curr.next  = prev
    #         prev = curr
    #         curr = temp
    #     self.head = prev
    

    def reverseLList(self):

        prev = None
        curr = self.head

        while(curr is not None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    
    def printRevUsingRec(self, out, headNode):
        
        if headNode is None:
            return
        self.printRevUsingRec(out, headNode.next)
        out.append(headNode.val)
        return out

    def forwardPrintingRecursion(self, out, headNode):

        if headNode is None:
            return
        out.append(headNode.val)
        headNode = headNode.next
        self.forwardPrintingRecursion(out, headNode)
        return out

    def recursionReverseLL(self, curr):

        if curr.next is None:
            self.head = curr
            return
        
        self.recursionReverseLL(curr.next)
        temp = curr.next
        temp.next = curr
        curr.next = None

        # if curr is None:
        #     self.head = prev
        #     return 
        # temp = curr.next
        # curr.next = prev
        # prev = curr
        # curr = temp
        # self.recursionReverseLL(curr, prev)
        

    def removeDuplicates(self):
        prev  = self.head
        curr  = self.head.next

        while(curr is not None):
            temp = curr.next

            if prev.val == curr.val:
                prev.next = temp
                curr =  temp
            else:
                prev = curr
                curr = temp
    
    def removeNthNodeFromEnd(self, n):


        temp = self.head
        curr = None
        prev = None
        l = 0

        while temp is not None:
            l += 1

            if l - n < 0:
                temp = temp.next
                continue
            elif l - n == 0:
                curr = self.head
                temp = temp.next
            else:
                prev = curr
                curr = curr.next
                temp = temp.next
        
        if prev is None:
            self.head = head.next
        else:
            prev.next = curr.next
        



        # l = 0
        # temp = self.head
        # while temp is not None:
        #     l += 1
        #     temp = temp.next

        # k = l - n

        # temp = self.head
        # prev = None
        # while k != 0:
        #     prev = temp
        #     temp = temp.next
        #     k -= 1

        # if prev is None:
        #     self.head = self.head.next
        # else:
        #     prev.next = temp.next

        

        # l = 0
        # temp = self.head
        # x = self.head



        # while temp.next is not None:
        #     if n - l >= 0:
        #         temp = temp.next
        #         continue
        #     else:
        #         x = x.next
            
        #     temp = temp.next
        
       
        # if n == 1:
        #     x = None
        # else:
        #     x.next = x.next.next


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



    
            




def main():

    llist = LinkedList()
    llist.appendNode(Node(1))
    llist.appendNode(Node(2))
    llist.appendNode(Node(3))
    llist.appendNode(Node(4))
    # llist.appendNode(Node(5))
    llist.swapNodeInPairs()
    llist.printNodes()
    #llist.removeNthNodeFromEnd(2)
    
    
    #llist.printNodes()
    #llist.removeDuplicates()
    #llist.printNodes()
    #llist.insertAt(0, Node(5))
    #llist.insertAt(4, Node(7))
    #llist.printNodes()

    #llist.deleteNodeAtIndex(0)
    #llist.printNodes()
    #temp = llist.head
    #out = []

    
    #print(llist.printRevUsingRec(out, temp))
    #print(llist.forwardPrintingRecursion(out, temp))
    #llist.recursionReverseLL(temp)
    #llist.reverseLList()
    #llist.printNodes()


    # llist.insertAt(1, Node(19))
    # llist.insertAt(5, Node(17))
    # llist.printNodes()

    # llist.deleteNode(19)
    # llist.printNodes()
    # llist.appendNode(Node(2))
    # llist.appendNode(Node(3))
    # llist.printNodes()
    
if __name__ == '__main__':
    main()

