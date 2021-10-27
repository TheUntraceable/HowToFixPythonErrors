# TypeError is raised when a function doesnt accept a specific type of object as an argument

def func(x: int):
    print(x - 1)

# in the above function we are specifying that x should be an int for the function to work perfectly
# but if we call the function with a string instead

func("a string")

# this would raise a TypeError since subtracting is not possible with strings
# An example error would look like this
# TypeError: unsupported operand type(s) for -: 'str' and 'int'
