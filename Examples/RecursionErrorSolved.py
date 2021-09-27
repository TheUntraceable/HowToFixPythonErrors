# So lets create a function

def func(x):
    return func(x)

# this would immediately raise RecursionError since calling this function will go on forever and ever
# you can see the maximum recurstion limit by printing sys.getrecursionlimit() like this

import sys
print(sys.getrecursionlimit())

# to fix a recursion error, add a base case.

def f(x):
    if x == 5:
        return x
    z = x + 1
    return f(z)

# the "if x == 5" in the above example is called a base case so we dont reach the max recursion limit
# now calling the function "f" will return 5
f(1)
