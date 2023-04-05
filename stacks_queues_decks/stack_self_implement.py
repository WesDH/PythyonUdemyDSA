class Stack(object):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.items == []:
            print("Cannot pop from stack, stack is empty.")
            return
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def peek(self):
        if self.items == []:
            print("Cannot peek stack, stack is empty.")
            return
        return self.items[-1]


new_stack = Stack()
print(new_stack.is_empty())
new_stack.push(300)
new_stack.push("this is a string")
new_stack.push(True)

print(new_stack.peek())

print(new_stack.size())

print(new_stack.pop())
print(new_stack.pop())
print(new_stack.pop())
print(new_stack.is_empty())
