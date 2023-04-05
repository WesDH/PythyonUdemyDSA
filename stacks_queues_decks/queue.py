class Queue(object):
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def pop(self):
        if self.items == []:
            print("Queue empty, nothing to remove!")
            return
        return self.items.pop(0)
    def is_empty(self):
        return self.items == []
    def peek(self):
        if self.items == []:
            print("Queue emptyiii, nothing to peek!")
        return self.items[len(self.items) - 1]]
    def size(self):
        return len(self.items

                )
