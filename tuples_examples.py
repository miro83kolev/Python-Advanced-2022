# tt = (1, 2, 3, 4, 6, 1, 2, 4, 5, 7)
# print(tt)
# print('-------count---------')
# print(tt.count(1))
# print(tt.count(3))
# print(tt.count(4))
#
#
# print('-------index---------')
# print(tt.index(1)) #equal to tt.index(1, 0)
# print(tt.index(1, 1))
#
# print('-------index---------')
# print(1 in tt)
# print(17 in tt)
#
# print('-------index---------')
# for value in tt:
#     print(value)
#
# print('-------list_comprehensions---------')
# [print(x) for x in tt]
#
# print('-------other_objects---------')
# print(f'str.join(): {", ".join(map(str, tt))}')
#
# print(len(tt)) # shows length of tuples
#
# print('-------tuples_concatenation---------')
# print((1, 2) + (3, 4, 5))
#
#
# for index, value in enumerate(tt):
#     print(f'tt{[index]}={value}')
#
# #equal to
#
# for index in range(len(tt)):
#     value = tt[index]
#     print(f'tt{[index]}={value}')

print('-------change_mutable_objects---------')
tt1 = ([1, 2, 3], {}, (1, 2, 5))
print(tt1)
tt1[0].append(5)
tt1[1] ["1"] = "2"
print(tt1)