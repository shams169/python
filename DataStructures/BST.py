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
        else:
            self.insertNode(temp, val)


    def insertNode(self, current, val):
        
        if current.data < val and current.left is not None:
            self.insertNode(current.left, val)
        elif current.data < val and current.left is None:
            current.left = Node(val)
        elif current.data > val and current.right is not None:
            self.insertNode(current.right, val)
        elif current.data > val and current.right is None:
            current.right = Node(val)
    

    def printTree(self):

s
        
        # q.put(self.root)

        # while(not q.empty):
        #     temp = q.get()
        #     print(temp.data)

        #     if temp.left:
        #         q.put(temp.left)
        #     if temp.right:
        #         q.put(temp.right)



def main():
    obj = BST()
    obj.insert(15)
    obj.insert(10)

    obj.printTree()

if __name__=='__main__':
    main()
    
    