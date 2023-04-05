#self implementation

class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.items == []:
            print("Cannot dequeue, queue empty")
            return
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []
    def peek(self):
        if self.items == []:
            print("cannot peek, queue empty)")
            return
        return self.items[0]


if __name__ == "__main__":
    q = Queue()
    print("is_empty():", q.is_empty())
    print("size(): ", q.size())
    print("enqueue 1: ", q.enqueue(1))
    print("enqueue: 2", q.enqueue(2))
    print("dequeue: ", q.dequeue())
    print("peek: ", q.peek())
    print("dequeue: ", q.dequeue())
    print("dequeue: ", q.dequeue())
    print("peek: ", q.peek())

            
            
