def area_rectangle(length, width):
    return length * width


def perimeter_rectangle(length, width):
    return length * 2 + width * 2


def rectangle(length, width):
    if length.isalnum() and width.isalnum:
        print(f'Rectangle area: {area_rectangle(length, width)}')
        print(f'Rectangle perimeter: {perimeter_rectangle(length, width)}')
    else:
        print('"Enter valid values!"')


print(rectangle('2', 10))