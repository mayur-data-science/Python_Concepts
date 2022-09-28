# More decorator examples:
# When you specify @variable_counter above any original function , the same original function will be passed as argument.
# It means decorator function accept only one function as input.


def variable_counter(input_function): #2
    # counter_remember.counter = 0 # UnboundLocalError: local variable 'counter_remember' referenced before assignment
    def counter_remember(*args,**kargs):#7 #14 21
        # counter_remember.counter = 0 # reinitalizng counter to 0 every time we call counter_remember() function so no meaning to write this line
        counter_remember.counter = counter_remember.counter + 1 #8 #15 #22
        return input_function(*args,**kargs)#9 #16 #23
                                            #12 --> return None 
                                            #19 --> return None
                                            #26 --> return None
    counter_remember.counter = 0    #3 
                                    # setting counter with zero
    
    return counter_remember #4 # returning counter_remember function type object reference variable.

@variable_counter #1 # automatically calling variable_counter(normal_function)
def normal_function(): #10 #17 #24
    pass #11 #18 #25

if __name__ == '__main__': # True #5
    normal_function() # calling counter_remember() #6 # None
    normal_function() # again calling counter_remember() #13 #None
    normal_function() # calling counter_remember() #20 # None
    print(normal_function.counter)  #27
                                    # printing counter variable of counter_remember() function.

# o/p: 3

# without decorator: as higher-order functions
# you can pass any number of functions as an argument to to variable_counter as its normal python function.
# what is the difference between higher Order Functions and decorator function.?
    # the main difference is Higher-Order-Function may take many input function and returns many output functions.
    # decorator function only take one input function and returns only one function as output.

def variable_counter(input_function): # input_function = normal_function. # Aliasing happned.
    # counter_remember.counter = 0 # UnboundLocalError: local variable 'counter_remember' referenced before assignment
    def counter_remember(*args,**kargs):
         # counter_remember.counter = 0 # reinitalizng counter to 0 every time we call counter_remember() function so no meaning to write this line
        counter_remember.counter = counter_remember.counter + 1
        return input_function(*args,**kargs)
    
    counter_remember.counter = 0
    return counter_remember    

def normal_function():
    pass

counter_remember = variable_counter(normal_function)

if __name__ == '__main__':
    counter_remember()
    counter_remember()
    counter_remember()
    print(counter_remember.counter)
#-----------------------------------------------------------------------------------------------------------------------

# Ex--> 2
# When you specify @decorator_function above any original function , the same original function will be passed as argument.
# It means decorator function accept only one function as input.


def decorator_function(input_func):#2  # input_function = remainder # Aliasing happned
    
    def wraper(a,b):#5
        print("Inside Wraper function")#6
        if b==0: # True #7
            print("argument b is 0") #8
            return #9 # return None # below line wont run # code after first return keyword is dead code
        return remainder(a,b)   # recursive call to wraper(a,b) # infinite loop # if above return statement commented.
                                # wont executing because its second return statement in this function.
    
    return wraper #3


@decorator_function #1
def remainder(a,b):
    return a%b

remainder(10,0) #4 # None

# o/p :  
#        Inside Wraper function
#        argument b is 0

# without decorator:
# you can pass any number of functions as an argument to to decorator_function as its normal python function.

def decorator_function(input_func):#2
    
    def wraper(a,b):#5
        print("Inside Wraper function")#6
        if b==0:# True #7
            print("argument b is 0")#8
            return #9
        return remainder(a,b)
    return wraper #3


def remainder(a,b):
    return a%b

remainder = decorator_function(remainder)#1

remainder(10,0)#4 # None

# o/p :  
#        Inside Wraper function
#        argument b is 0
#------------------------------------------------------------------------------------------------------

# Ex-->3

def check_zero(func): # func = div # aliasing happned

    def wrap(num1, num2):
        
        if num2 == 0: # if block
            return "Undefined"
                # calling div(a,b)
        return func(num1, num2) # returning data
    
    return wrap

@check_zero
def div(a, b):
    return a/b # returning data

print(div(div(4, 2), div(0, 10)))   # calling wrap(4, 2) ==> 2.0
                                    # calling wrap(0, 10) ==> 0.0
            # 2.0  ,    # 0.0

# o/p : Undefined


# without decorator:

def check_zero(func):

    def wrap(num1, num2):
        
        if num2 == 0:
            return "Undefined"
        
        return func(num1, num2)
    return wrap


def div(a, b):
    return a/b

div = check_zero(div)
print(div(div(4, 2), div(0, 10)))

#----------------------------------------------------------------------------

# Ex--> 4
# in program we can specify decorator to any function for extended functionality insted of running original function
# (we may or may not call original function inside decorators wraper function)
def decorator(input_function):  # input_function = square or
                                # input_function = square_root

    def wraper(*args, **kwargs):

        list = [pow(x, 2) for x in args] # Square of input Arguments
        return input_function(list, **kwargs)   # calling original function's 
                                                # square(list) or square_root(list) depends which one is input function to decorator.

    return wraper

@decorator # calling decorator with input function as square # returning wraper # assigning wraper to square # now we can call wraper by using its aliase name square.
def square(list):
    return list # returning list as it is.

@decorator # calling decorator with input function as square_root # returning wraper # assigning wraper to square_root # now, we can call wraper by using its aliase name square_root.
def square_root(list):
    return [pow(x, 0.5) for x in list] # doing square root of input list data and returning.

def function3():
    print(square(1, 2, 3, 4), square_root(1, 2), square(1, 2), square_root(1, 2, 3, 4))

function3()

# o/p : [1, 4, 9, 16] [1.0, 2.0] [1, 4] [1.0, 2.0, 3.0, 4.0]
