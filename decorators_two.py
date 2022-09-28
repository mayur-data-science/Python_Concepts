# More decorator examples:
# When you specify @decorator_function above any original function , the same original function will be passed as argument.
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

# without decorator:
# you can pass any number of functions as an argument to to variable_counter as its normal python function.

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