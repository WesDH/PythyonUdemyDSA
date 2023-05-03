class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3

    cur = node1

    while cur is not None:
        print(cur.item)
        cur = cur.next
