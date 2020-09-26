"""
Stack implementatio using a list 
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def printStack(self):
        return self.stack

    def push(self, val):
        self.stack.append(val)
        self.top += 1

    def pop(self):
        x = self.stack.pop()
        self.top -= 1
        return x

    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False

    def getTop(self):
        return self.stack[len(self.stack)-1]
    
    

    
def main():
    obj = Stack()
    #obj.push(4)
    #obj.push(5)
    #obj.push(6)
    #obj.push(9)
#
    #obj.pop()
    #obj.pop()
    #obj.pop()
    #print(obj.printStack())
    #obj.pop()
#
    S = 'HELLO'

    for c in S:
        obj.push(c)
    print(obj.printStack())

    out = ''
    while(obj.top >= 0):
        out += obj.pop()

    print(out)
    print(obj.isempty())



if __name__ == '__main__':
    main()
