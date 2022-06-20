def say_hello(n=5):
    if n == 0:
        return
    print('Hello')
    say_hello(n-1)

say_hello()