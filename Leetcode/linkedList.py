#!/usr/bin/env python3


# Node class to create nodes for the linkedlist
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, node):
        if self.head == None:
            self.head = node
            self.size += 1
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
            self.size += 1
        
    def printNodes(self):

        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

            
    
    def insert(self, index, node):

        if self.size < index:
            print("Invalid index")
            return
        
        temp = self.head
        counter = 0
        if index == 0:
            node.next = temp.next
            self.head = temp
        while(temp.next != None):
            if counter+1 == index:
                node.next = temp.next
                temp.next = node
                break
        self.size += 1        


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    llist = LinkedList()
    llist.append(node1)
    llist.append(node2)
    llist.append(node3)
    llist.printNodes()
    print('-----------------------')
    llist.insert(1, Node(5))

    llist.printNodes()
    
   

if __name__ == '__main__':
    main()