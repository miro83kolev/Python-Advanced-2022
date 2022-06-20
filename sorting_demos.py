from audioop import reverse

values = [1, 3, 10, 898, -11, -43]

print(values)
print(sorted(values))
# creates new list
values.sort()
# sorts the list
print(values)

#sorted works with dict, tuple, lists


def order_by_reminder_2(x):
    return x % 2

print(sorted(values, key=lambda x: x % 2))
# sorted by modular division of 2 nums
print(sorted(values, reverse=True))
# sorted in reversed order
print(sorted(values, key=order_by_reminder_2, ))
# sorted by modular division of 2 nums w/o using lambda
print(sorted(values, key=lambda x: (x % 2, x)))
# sorted by modular division of 2 nums in sorted order using tuple

#sorted dict

dd = {
    'Ivan': 18,
    'Gosho': 28,
    'John': 48,

}

print(sorted(dd.items()))
#sorts alphabetically by keys
print(sorted(dd.items(), reverse=True))
#sorted reversed alphabetically
print(sorted(dd.items(), key=lambda x: x[1]))
#sorts by values in keys ascending
print(sorted(dd.items(), key=lambda x: x[1], reverse=True))
#sorts descending by values in keys