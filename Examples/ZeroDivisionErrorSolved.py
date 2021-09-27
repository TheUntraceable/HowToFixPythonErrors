# lets say u ask for a user input like this

user_input = int(input("Enter a number: "))

# and they input 0...

value = 10 / user_input

print("10 divided by", user_input, "is,", value)

# this will raise the error saying you cant divide by 0
# an easy and good way to handle this is by using an if statement to check if its 0 or not

if user_input == 0:
    print("Invalid number input")
else:
    value = 10 / user_input
    print("10 divided by", user_input, "is,", value)
