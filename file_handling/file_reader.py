# print(sum([int(x) for x in open('./numbers.txt')]))
file = open('./numbers.txt')
print(sum([int(x) for x in file]))