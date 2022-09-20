# Nested Functions:
          # Nested function means function inside function.
          # Nested functions are local to outer function, from outside we can't call directly.

def outer_function():# outer_function declared
    print("outer_function started")

    def inner_function(): # inner_function declared
        print("inner_function started")
    
    inner_function() # inner_function called
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

to_call_inner_function = outer_function() # outer_function called and retuned...
                                          # ...inner_ function i.e "<function outer_function.<locals>.inner_function at 0x0000018C99D8AEF0>"
                                          # Here internally function aliasing happned, capturing returned value in "to_call_inner_function" variable.
                                          # now, "to_call_inner_function" acts as referance variable pointing to "inner_function()"
print(to_call_inner_function) # o/p: "<function outer_function.<locals>.inner_function at 0x000001DAE778AEF0>"
to_call_inner_function() # Now, happily we can call inner_function() from...
                         # ...outside of "outer_function()" by using its aliase name i.e "to_call_inner_function"
#-------------------------------------------------------------------------------------------------------------------------------------------------