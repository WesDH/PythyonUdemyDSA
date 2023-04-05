class Deque(object):
    def __init__(self):
        self.items = []
    def add_rear(self, item):
        self.items.append(item)
    def add_front(self, item):
        self.items.insert(0, item)
    def rm_rear(self):
        if self.items == []:
            print("Deque empty! nothing to remove!")
            return
        return self.items.pop()
    def rm_front(self):
        if self.items == []:
            print("Deque empty! nothing to remove!")
            return
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []

if __name__ == "__main__":
    d = Deque()
    print("Add Hello to front")
    d.add_front("Hello")
    print("Add World to rear")
    d.add_rear("World")
    print("d.size(): ", d.size())
    print("rm front and rm rear: ", d.rm_front(), d.rm_rear())
    print("d.size(): ", d.size())
    print("d.is_empty(): ", d.is_empty())
