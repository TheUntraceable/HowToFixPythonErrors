# Lets use the following dictionary as an example

d = {
    "key" : "value"
}

# and then you do this

print(d["doesnt exist"])

# that obviously would raise KeyError: doesnt exist
# you can add it manually like this

d["doesnt exist"] = "value"

# or if possible, add it during the creation like this

d = {
    "key" : "value",
    "now exists" : "value"
}

# if adding the key isnt an option, use dict.get and avoid the error

value = d.get("Key doesnt exist")
print(value)

# the above code would output 'None' since the key "Key doesnt exist" is not in the dictionary
