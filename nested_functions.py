def math_operations_factory(operation, *args):
    def add(*args):
        result = sum(args)
        return result

    def subtract(*args):
        result = sum([-x for x in args])

