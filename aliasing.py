# Aliasing :
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