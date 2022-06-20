ss = {2, 3, 4, 5}
print(ss)
[ss.add(1) for _ in range(10)]
print(ss)

#add
ss.add(8)
print(ss)

#remove
ss.remove(2)
print(ss)

#show value in assert
print(4 in ss)
print(9 in ss)