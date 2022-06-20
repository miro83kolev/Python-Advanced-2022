def math_ops(sign, *args):
    if sign == "+":
        result = sum(args)
    elif sign == "*":
        result = 1
        for x in args:
            result *= x
    elif sign == '-':
        result = -sum(args)
    elif sign == '/':
        result = 1
        for x in args:
            result /= x
    elif sign == '^':
        result = 1
        for x in args:
            result = x * args
    return result

print (math_ops('^', 1, 2, 4))