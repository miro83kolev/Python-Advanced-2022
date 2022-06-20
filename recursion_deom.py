def f1():
    f1()

#function calls itself
#you must have base something to break the recursion like in while loop
def reversed_loop(n):
    if n < 0: # base or exit case
        return

    print(n)
    reversed_loop(n - 1) # recursive call

reversed_loop(6)

def forward_loop(n):
    if n < 0: # base or exit case
        return

    forward_loop(n - 1)  # recursive call - be careful where you put you recursive call
    print(n)


forward_loop(6)
