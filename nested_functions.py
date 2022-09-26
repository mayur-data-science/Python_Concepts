# nested functions and closure in python :
#-------------------------------------------------------------------------------------------------------------
# Nested Functions:
            # Nested function means function inside function.
            # Nested functions are local to outer function, from outside we can't call directly.
            # If a function is not returning any thing, the default returned value is "None"

def outer_function():# outer_function declared
    print("outer_function started")

    def inner_function():   # inner_function declared 
                            # inner_function() enclosing scope is outer_function() local scope.
        print("inner_function started")
    
    inner_function()    # inner_function called
                        # inner_function() locally available to outer_function()
                        # we can call inner_function() inside outer_function()
                        # but we can not call inner_function from outside of outer_function()
                    
    print("outer_function finished")

outer_function() # outer_function called
# inner_function() # NameError: name 'inner_function' is not defined.

# o/p:  outer_function started
#       inner_function started
#       outer_function finished
#----------------------------------------------------------------------------------------------

# There is a way to call inner_function() from outside of outer_function()

# A function can return another function.

def outer_function(): # outer_function declared
    print("outer_function started")

    def inner_function(): # inner_function declared
        print("inner_function started")
    
    print("outer_function returned: ", inner_function)
    return inner_function # outer_function() returned inner function i.e "<function outer_function.<locals>.inner_function at 0x0000018C99D8AEF0>"
    return inner_function() # its a function call, inner_function() will retun none
to_call_inner_function = outer_function()   # outer_function called and retuned...
                                            # ...inner_ function i.e "<function outer_function.<locals>.inner_function at 0x0000018C99D8AEF0>"
                                            # Here internally function aliasing happned, capturing returned value in "to_call_inner_function" variable.
                                            # now, "to_call_inner_function" acts as referance variable pointing to "inner_function()"
print(to_call_inner_function)   # o/p: "<function outer_function.<locals>.inner_function at 0x000001DAE778AEF0>"
to_call_inner_function()    # Now, happily we can call inner_function() from...
                            # ...outside of "outer_function()" by using its aliase name i.e "to_call_inner_function"
#-------------------------------------------------------------------------------------------------------------------------------------------------

# Example 1 :

# Parameter's : A parameter's are the variable listed inside the parentheses in the function definition
# Argument's  : argument's are the value that are sent to the function when it is called
# *args (Non-Keyword Arguments): to pass a variable(any) number of arguments to a function from function call.
# **kwargs (Keyword Arguments) : to pass a variable(any) number of arguments to a function from function call.
        # Note : Name after * or ** can be anything but it is recomanded to use args and kwargs as industry standerd.

def outer_function(*args): 
    
    def add(*args): # Parameter
        return user_input1 + user_input2
    
    def sub(*args):
        return user_input1 - user_input2
    
    def mul(*args):
        return user_input1 * user_input2
    
    def div(*args):
        return user_input1 / user_input2
    
    def mod(*args):
        return user_input1 % user_input2 
    
    return add, sub, mul, div, mod

while True:
    try:
        user_input1 = int(input("Enter first number : "))
        user_input2 = int(input("Enter second number : "))
        break
    except ValueError as ex:
        print("Please dont enter letters or words only enter number : ", ex)
        continue
                

# tuple = outer_function(user_input1, user_input2) # returned Functions packed in tuple
# print(tuple)

add1, sub1, mul1, div1, mod1 = outer_function(user_input1, user_input2) # returned Functions in form of tuple, unpacking from left to right.

print(
    "Addition : {} \nSubtraction: {} \nMultiplication : {} \nDivision : {} \nRemainder : {} ".
    format(add1(), sub1(), mul1(), div1(), mod1())
    )   # The format() method formats the specified value(s) and insert them inside the string's placeholder from left to right. 
        # The placeholder is defined using curly brackets: {}.
print("*"*20)
print("Remainder : {4} \nDivision: {3} \nMultiplication : {2} \nSubtraction : {1} \nAddition : {0} ".format(add1(), sub1(), mul1(), div1(), mod1()))
# you can also use index in place holder, in this way we get the flexiblity to provide arguments to format() function.

#---------------------------------------------------------------------------------------------------------------------------------------------
# Example 3:
def outer_mean(): # Function declared
    sample = [] # Initially empty list assigned to sample referance variable.
    def inner_mean(number): # Function declared
        sample.append(number) # appending number  to sample list
        return sum(sample) / len(sample), number# sum(sample)--> calculating sum in sample list.
                                                # len(sample)--> calculating length of sample list.
                                                # we are dividing to calculating mean from sample list.
                                                # finally returning the mean value and (input data) number
    return inner_mean, sample # returning the inner_mean function and sample list.

sample_mean, sample = outer_mean()  # outer_mean() returning the inner_mean() function type object and we are assigning to sample_mean referance variable which is now pointing to inner_mean() function
                                    # also outer_mean() function returning "sample" list.
del outer_mean # deleted outer_mean referance variable for function type object.

# inner_mean() function type object that remembers values of its enclosing scopes(outer_mean() scope).
# When you call outer_mean(), you’re also creating a local scope,...
# ...The local scope of outer_mean() is, at the same time, the enclosing scope of inner_mean(). 
# From inside inner_mean(), this scope is neither the global scope nor the local scope. 
# It’s a special scope that lies in between those two scopes and is known as the "enclosing scope".

print(sample_mean(100)) # o\p: (100.0, 100) 
                        # calling inner_mean() function of outer_mean() function using referance variable sample_mean. and printing it.
print(sample_mean(105)) # o\p: (102.5, 105)
print(sample_mean(102)) # o\p: (102.33333333333333, 102)
print(sample)       # o/p: [100, 105, 102] # printing sample list.
                    # inner_mean() function now new referance variable called sample_mean...
                    # ...which remembers the variables of outer_mean() i.e "sample" list. 
print(sample[2])    #o/p: 102 # accessing 2nd indexed value from "sample" list.

mean, number = sample_mean(200) # unpacking returned values of sample_mean() i.e inner_mean() in mean and number
print(sample) # o/p: [100, 105, 102, 200]
print(mean)   # o/p: 126.75
print(number) # o/p: 200
#outer_mean()   # NameError: name 'outer_mean' is not defined 
                # because we deleted outer_mean referance variable of that function object. 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
