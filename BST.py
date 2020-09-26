#!/usr/bin/env
from queue import Queue
import os

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:

    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        temp = self.root
        if self.root is None:
            self.root = Node(val)
            print('Inserting the root node: {}'.format(val))
        else:
            self.insertNode(temp, val)

    def findHeight(self):
        if self.root is None:
            return -1
        return max(self.findTreeHeight(self.root.left), self.findTreeHeight(self.root.right)) + 1 
    
    def findTreeHeight(self, current):

        if current is None:
            return -1

        
        height = max(self.findTreeHeight(current.left),
                    self.findTreeHeight(current.right)) + 1
        print('Height of {}: {}'.format(current.data, height))
        return  height

    def insertNode(self, current, val):
        if val < current.data:
            if current.left:
                self.insertNode(current.left, val)
            else:
                current.left = Node(val)

        elif val > current.data:
            if current.right:
                self.insertNode(current.right, val)
            else:
                current.right = Node(val)
    
    def preOrder(self):
        current = self.root

        if current is None:
            return None
        
        print(current.data)

        if current.left:
            self.preOrderTraversal(current.left)
        if current.right:
            self.preOrderTraversal(current.right)
    
    def preOrderTraversal(self, current):

        if current is None:
            return
        
        print(current.data)
        if current.left:
            self.preOrderTraversal(current.left)
        if current.right:
            self.preOrderTraversal(current.right)
    
    def inOrder(self):
        current = self.root

        if current is None:
            return
        
        if current.left:
            self.inOrderTraversal(current.left)
        
        print(current.data)
        
        if current.right:
            self.inOrderTraversal(current.right)
    
    def inOrderTraversal(self, current):

        if current is None:
            return

        if current.left:
            self.inOrderTraversal(current.left)
        
        print(current.data)
        
        if current.right:
            self.inOrderTraversal(current.right)


    # This is an iterative apporach for inorder traversal
    def inOrderIterative(self):
        
        curr = self.root
        nodeStack = []

        while(curr or nodeStack):

            if curr is not None:
                nodeStack.append(curr)
                curr = curr.left
            else:
                curr = nodeStack[-1]
                nodeStack.pop()
                print(curr.data)

                curr = curr.right

    # preOrder Iterative Solution
    def preOrderIterative(self):
        curr = self.root
        nodeStack = []

        while(curr or nodeStack):

            if curr is not None:
                print(curr.data)
                nodeStack.append(curr)
                curr = curr.left
            else:
                curr = nodeStack[-1]
                nodeStack.pop()
                curr = curr.right
        
    def deleteNode(self):
        pass

    def printTree(self):
        q = Queue()
        q.put(self.root)
        while(not q.empty()):
            temp = q.get()
            print(temp.data)

            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)



def main():
    obj = BST()
    obj.insert('F')
    obj.insert('D')
    obj.insert('J')
    obj.insert('K')
    obj.insert('G')
    obj.insert('E')
    obj.insert('B')
    obj.insert('C')
    obj.insert('A')
    #print(obj.findHeight())
    obj.preOrder()
    #obj.inOrderIterative()
    print('----------------')
    obj.preOrderIterative()


    #obj.printTree()

if __name__=='__main__':
    main()
    
    