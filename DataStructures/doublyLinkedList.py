class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoubleLinkedList:

    def __init__(self, head=None):
        self.head = head
    
    def insertAtHead(self, val):
        newNode = Node(val)

        if self.head == None:
            self.head = newNode
            return
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        return
    
    def printNodes(self):
        
        temp = self.head
        out = []
        while(temp is not None):
            out.append(temp.val)
            temp = temp.next
        print(out)
    
    def reversePrint(self):
        temp = self.head
        out = []
        
        if temp == None:
            return out
        
        while(temp.next != None):
            temp = temp.next

        while(temp is not None):
            out.append(temp.val)
            temp = temp.prev 
        return out

def main():
    obj = DoubleLinkedList()
    obj.insertAtHead(1)
    obj.insertAtHead(2)
    obj.insertAtHead(4)
    obj.insertAtHead(8)
    obj.printNodes()
    print(obj.reversePrint())

if __name__ == '__main__':
    main()