# ValueError is raised when a function or operation does accept an argument of that type
# but it just doesnt accept this value.
# By default calling `int` would return an integer with base 10.

a = int("8")

# Now the variable a is an integer 8 with base 10. We can also see that it accepted a string as the first 
# argument

b = int("bunch of letters")

# but calling it like the above example will raise error since a bunch of letters cannot be interpreted 
# as an integer with base 10.

# Example Error:
# ValueError: invalid literal for int() with base 10: 'a'
