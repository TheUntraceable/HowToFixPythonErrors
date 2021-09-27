# Got code like this that raises 'IndentationError: expected an indented block'?

def function():

print("Hello")

# Indent the print("Hello") line by pressing one tab or 4 spaces and you should be fine

# Code says 'IndentationError: unexpected indent' instead?

def function():
    print("Test")
        print("Error")

# unindent the print("Error") line and get it to the same indentation as the line above. like this

def function():
    print("Test")
    print("No Error")

# Note that using both tabs and spaces will raise TabError
