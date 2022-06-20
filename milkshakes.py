from collections import deque

choco = [int(x) for x in input().split(', ')]
cups = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while choco and cups and milkshakes < 5:
    one_choco = choco.pop()
    one_cup = cups.popleft()

    if one_choco <= 0 and one_cup <= 0:
        continue

    if one_choco <= 0:
        cups.appendleft(one_cup)
        continue

    if one_cup <= 0:
        choco.append(one_choco)
        continue

    if one_choco == one_cup:
        milkshakes += 1
    else:
        cups.append(one_cup)
        choco.append(one_choco - 5)

if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')

if choco:
    print(f'Chocolate: {", ".join([str(x) for x in choco])}')
else:
    print(f'Chocolate: empty')

if cups:
    print(f'Milk: {", ".join([str(x) for x in cups])}')
else:
    print(f'Milk: empty')


