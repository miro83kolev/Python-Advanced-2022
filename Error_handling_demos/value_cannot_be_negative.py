class ValueCannotBeNegative(Exception):
    pass


values = [int(input()) for x in range(5)]

for value in values:
    if value < 0:
        raise ValueCannotBeNegative