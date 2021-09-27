# Lets say we define a function like this

def func():
    # and then we try to print an undefined variable
    print(f)
    # but we assign it later inside the function
    f = "Hello World!"

# the above code will raise UnboundLocalError: local variable 'f' referenced before assignment
