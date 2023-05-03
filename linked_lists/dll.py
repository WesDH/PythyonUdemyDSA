class Node(Object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    
    a.next = b
    b.prev = a

    b.next = c
    c.prev = b
