import time

stack = []

count = 2 ** 18
result = 0

start = time.time()
for i in range(count):
    stack.append(i)

while stack:
    result += stack.pop()

end = time.time()

print(end - start)

for i in range(count):
    stack.insert(0, i)

while stack:
    result += stack.pop(0)

end = time.time()

print(end - start)