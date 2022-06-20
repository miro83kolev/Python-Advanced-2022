# #ALL STACK OPERATIONS
#
# #push on stack
#
# stack = [1, 3, 5, 6, 7]
# stack.append(9)
# print(stack)
#
# #peek on stacks
#
# stack = [1, 3, 5, 6, 7]
# print(stack.pop()) # 7 is removed from stack
# last_el = stack[-1]
# print(last_el) # gives 6 which is the last_el on stack
#
#
# #pop on stack
# stack = [1, 3, 5, 6, 7]
# stack.pop()
# stack.pop()
# print(stack)
#
# #len stack
# stack = [1, 3, 5, 6, 7]
# print(len(stack)) # gives 5
# stack.pop() # remove last element from stack
# print(len(stack)) # gives 4 as length

class Stack:
    def __int__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]


    def length(self):
        return len(self.values)

s = Stack()

for v in range(5, 10):
    s.push(v)

print(s.pop())
print(s.peek())
print(s.length())
