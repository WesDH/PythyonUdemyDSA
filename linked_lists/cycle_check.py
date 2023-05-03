from ll import *
from nose.tools import assert_equal

if __name__ == "__main__":
    def check_cycle(node):
        #node_list = []
        #while cur is not None:
        #    if cur in node_list:
        #        return True
        #    node_list.append(cur)
        #    cur = cur.next
        #return False
        slower = node
        faster = node
        while faster is not None and faster.next is not None:
            slower = slower.next
            faster = faster.next.next
            if faster == slower:
                return True

        return False




    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.next = b
    b.next = c
    c.next = a # cycle created

    x = Node(8)
    y = Node(9)
    z = Node(10)

    x.next = y
    y.next = z  # No cycle (False)

    j = Node(1)  # No cycle (False)
    k = Node(2)

    j.next = k

    class TestCycleCheck(object):
        def test(self, sol_func):
            assert_equal(sol_func(a), True)
            assert_equal(sol_func(x), False)
            assert_equal(sol_func(j), False)
            print("ALL TESTS PASSED")


    # Run tests:
    t = TestCycleCheck()
    t.test(check_cycle)
