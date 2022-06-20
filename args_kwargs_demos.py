def f2(x, *args, **kwargs):
    print(f'x = {x}, args = {args}, kwargs = {kwargs}')

f2(1) # x accepts 1
f2(1, 2) # x accepts 1 and args accepts 2
f2(1, 2, 3) # x accepts 1 and args accepts 2, 3
f2(x=11, y=12) # x accepts 11 and kwargs accepts 12

#unpacking

ll1 = [1, 3, 5, 6]
k, l, *r = ll1 # k = 1, l = 2 and r packs 5,6

print(k, l, r)

ll2 = [-1, *ll1, -10] # unpacks ll1 [5, 6]
print(ll2)

dd1 = {
    'x': 1,
    'y': 2
}

print(dd1) # normal dict

dd2 = {
    'z': 3,
    **dd1,
}

print(dd2) # adding packed dict 1