sublists = input().split('|')

result = []

for idx in range(len(sublists) - 1, -1, -1):
    current_elements = sublists[idx].strip().split()
    result.extend(current_elements)

print(' '.join(str(x) for x in result ))