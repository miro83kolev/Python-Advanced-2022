def operate(operation, *args):
    def add(*args):
         result = sum(args)
         return result

    def subtract(x, *args):
         result = x + sum([-x for x in args])
         return result

    def multiply(*args):
         result = 1
         for el in args:
             result *= el

         return result

    def divide(x, *args):
        result = x
        for el in args:
            result /= el

        return result

    if operation == '+':
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    elif operation == '/':
        return divide(*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))


