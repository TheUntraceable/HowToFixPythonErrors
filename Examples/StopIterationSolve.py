
# Lets create a generator

def generator():
    for i in range(3):
        yield i

generator_object = generator()

next(generator_object) 
# will output 0

# Now if we close the generator by doing

generator_object.close()

# or let it finish iterating by doing

next(generator_object) # Outputs 1
next(generator_object) # Outputs 2

# And then do

next(generator_object)

# It would raise StopIteration since the generator has completed yielding
# now you either have to create a new object like

new = generator()

# or just stop iterating through it.

# NOTE: You can only iterate through generators once
