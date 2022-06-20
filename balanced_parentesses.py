expression = input()

opening_brackets = []

pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}

balanced = True

for ch in expression:
    if ch in '([{':
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
    else:
        last_opening_bracket = opening_brackets.pop()
        if pairs[last_opening_bracket] != ch:
            balanced = False
            break
    if not balanced:
        break

if balanced:
    print("YES")
else:
    print("NO")