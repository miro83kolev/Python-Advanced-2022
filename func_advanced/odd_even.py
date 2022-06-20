def even_odd(*args, **kwargs):
    even_nums = []
    odd_nums = []
    if kwargs.keys() == "even":
        for num in args:
            if num % 2 == 0:
                even_nums.append(num)
            else:
                odd_nums.append(num)
        print(even_nums)
        print(odd_nums)

print(even_odd(1, 2, 3, 4, 5, 6, "even"))