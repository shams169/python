class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class LinkedListStack:
    def __init__(self, top=None):
        self.top = top

    
    def push(self, val):
        newNode = Node(val)
        
        if self.top == None:
            self.top = newNode
            return
        else:
            newNode.next = self.top
            self.top = newNode
    
    def pop(self):
        temp = self.top
        self.top = temp.next
    
    def getTop(self):
        return self.top.val
    
    def isEmpty(self):
        if self.top:
            return True
        else:
            return False

    def printStack(self):

        temp = self.top
        out = []
        while temp is not None:
            out.append(temp.val)
            temp = temp.next
        print(out)


def main():
    obj = LinkedListStack()
    print(obj.isEmpty())
    obj.push(2)
    obj.push(3)
    obj.push(25)
    obj.push(9)
    obj.push(10)
    obj.printStack()
    obj.pop()
    print(obj.isEmpty())
    obj.printStack()

if __name__ == "__main__":
    main()   
    
    
