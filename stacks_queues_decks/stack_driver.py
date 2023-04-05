from stack import *
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
