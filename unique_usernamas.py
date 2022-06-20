n = int(input())
unique_usernames = set()

for _ in range(n):
    username = input()
    if username not in unique_usernames:
        unique_usernames.add(username)

print('\n'.join(unique_usernames))

# for user in unique_usernames:
# print(username)
#print(hash(username))