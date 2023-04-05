class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.items == []:
            print("Queue empty, nothing to remove!")
            return
        return self.items.pop(0)
    def is_empty(self):
        return self.items == []
    def peek(self):
        if self.items == []:
            print("Queue empty, nothing to peek!")
            return
        return self.items[0]
    def size(self):
        return len(self.items)


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
