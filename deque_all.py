from collections import deque

q = deque()
#enqueue, push, add
q.append(2) #appendRight
q.append(3)
q.append(4)
print(q)
# could be appendleft
q.appendleft(5)
print(q)

#pop, remove, dequeue
#if you use append you must use popleft to remove, if you you appendleft you use pop==popright

print(q.popleft())

#peek
print(q[0])

#count, length
print(len(q))
