

class MyQueue:

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.queue = []
        

    def enqueue(self, x):
        if self.isFull():
            print("Queue is Full cannot insert")
            return
        else:
            self.queue.append(x)
    
    def dequeue(self):
        if self.isEmpty():
            print("No elements in the queue")
            return 
        else:
            self.queue.pop(0)


            
    
    def isFull(self):
        return self.max_size == len(self.queue)

    def isEmpty(self):
        return (self.queue is None)


    def printQueue(self):
        print(self.queue)

def main():
    obj = MyQueue()
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)
    obj.enqueue(5)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)
    obj.enqueue(5)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.printQueue()

if __name__ == "__main__":
    main()