# There is no way of "fixing" KeyBoardInterrupt error so we would use a try-except block
# to bypass it when it is raised

def main():
    try:
        user_input = input(
        "What is your name?\n"
        "Note: Press ctrl + c to exit\n"
        "> "
        )
    except KeyboardInterrupt:
        # handle the error however you want to
        # but here, we would just ignore it and return
        return
    else:
        # else clause is executed if no error was raised
        print("Hello", user_input)

# and now we call our function
main()
# Now the output of it would look something like this

# What is your name?
# Note: Press ctrl + c to exit
# > Marcus <- this is our input
# Hello Marcus

# Instead, if we pressed ctrl + c when we were prompted, 
# it would have just end the process there and exit
