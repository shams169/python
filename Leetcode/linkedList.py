class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = None

    def addNode(self, Node):
        iter = self.head    
        while(iter.next == None):
            iter = iter.next

        iter.next = Node()


def main():
    obj = LinkedList()
    obj.addNode(Node(1))
    obj.addNode(Node(2))
    print(obj.head)

if __name__ == '__main__':
    main()