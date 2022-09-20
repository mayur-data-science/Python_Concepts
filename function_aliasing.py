# In python programming, the second name given to a piece of data is known as an alias. 
# Aliasing happens when the value of one variable is assigned to another variable because variables are just names that store references to actual value.
# Example:

first_variable = "PYTHON"
print("Value of first:", first_variable) # Value of first: PYTHON
print("Reference of first:", id(first_variable)) # Reference of first: 2610710821296 

print("--------------")

second_variable = first_variable # making an alias
print("Value of second:", second_variable) # Value of second: PYTHON
print("Reference of second:", id(second_variable)) # Reference of second: 2610710821296 

print("--------------")

# In python everything is treated as an object
# Even functions also internally treated as object only
# proof: 

def add():
    print("hello world")

print(add) # <function add at 0x000001BD7778AF80>
# "add" is an referance variable which is pointing to "function" type object "at" so and so location.
print(id(add)) # 1913264844672
# on this(0x000001BD7778AF80) location id(1913264844672) is located.

# Can we create another referance variable for add() function?
# YES, why not, we can create another referance variable..
# ..which is pointing to same function type object which already add reference variable is pointing.

add1 = add # what ever object pointed by add, for same object can you please assign add1 refrance variable also
print(add1) # <function add at 0x000001BD7778AF80>
print(id(add)) # 1913264844672
# now add1 referance variable also pointing to the same object which add is pointing to.
# This is called function aliasing.
add() # calling function add at 0x000001BD7778AF80 location.
# or you can also call like.
add1() # calling function add at 0x000001BD7778AF80 location.
# FUNCTION ALIASING:
#        For existing function we can give another name this is nothing but function aliasing