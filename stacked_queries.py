stack = []

n = int(input())

for _ in range(n):
    query_parts = [int(x) for x in input().split()]
    command = query_parts[0]

    if command == 1:
        number = query_parts[1]
        stack.append(number)
    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))

print(', '.join(reversed([str(x) for x in stack])))



