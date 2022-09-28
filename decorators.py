# Decorators:
#         Decorator is a function which can take function as an argument and extend it's functionality
#         and returns modified function with extended functionality.
# Decorator:
#---------->It is a function.
#---------->It always takes a function as an argument(input function)(only one)
#---------->It will create a new function with extended functionality.
#           In this new function we may use original function(input function)
#---------->It will return that extended function as output

# Without effecting original function, we can extended its functionality by using decorator.

# Ex--> 1:

def person_decorator(input_func): # marriage_proposal_meeting = input_func # function aliasing happned
    
    print("Memory location of person_decorator() : ",id(person_decorator))
    
    print("Memory location of (input_func) original marriage_proposal_meeting() : ",id(input_func))
    
    def decorating_person(): # creating new function with extended functionality.
        # In this new function we may use "marriage_proposal_meeting" function using its aliase name input_func
        # in this example we are not using input function(input_func).
        print("send person to beauty parlour")
        print("showing a person with full decoration")
        print("Memory location of decorating_person () : ",id(decorating_person))
    
    
    
    return decorating_person # returning decorating_person function with extended functionality as output.


@person_decorator # [1]calling "automatically" person_decorator(marriage_proposal_meeting) function using @(at the rate) annotation without executing marriage_proposal_meeting()
def marriage_proposal_meeting():    #[0] when control comes here and PVM checks if there is any decorator linked with this function decalaration
                                    # if YES, call [1] person_decorator i.e[@person_decorator] with argument "marriage_proposal_meeting".
                                    # person_decorator() function will return decorating_function() object in referance variable "decorating_person"  with extended functionality as output 
                                    # and "automatically" assign referance variable "decorating_person" object to referance variable(which is having same name as passed function name  i.e marriage_proposal_meeting ) 
    print("Showing a person as it is")

marriage_proposal_meeting() # then we can call decorating_person() function by using its aliase name "marriage_proposal_meeting" referance variable.
                            # internally calling decorating_person() function

print("Memory location of marriage_proposal_meeting : ",id(marriage_proposal_meeting))

# o/p :
    # Memory location of decorator_function() :  1556776651936
    # Memory location of (input_func) original marriage_proposal_meeting() :  1556776654240
    # send person to beauty parlour
    # showing a person with full decoration
    # Memory location of decorating_person() :  1556776654672
    # Memory location of marriage_proposal_meeting() :  1556776654672

# you can see that, memory location of decorating_person() function and marriage_proposal_meeting referance variable are same.
# it means internally decorating_person() and marriage_proposal_meeting referance variable pointing to same function type object.
#---------------------------------------------------------------------------
# internal implementation of decorator.
# this is how decorator works.
def person_decorator(input_func): # input_func = marriage_proposal_meeting
    
    print("Memory location of person_decorator() : ",id(person_decorator))
    
    print("Memory location of (input_func) original marriage_proposal_meeting() : ",id(input_func))
    
    def decorating_person(): # inner function.
        
        # In this new function we may use or call "marriage_proposal_meeting()" function using its aliase name input_func
        # in this example we are using input function(input_func).
        print("send person to beauty parlour")
        print("showing a person with full decoration")
        print("Memory location of decorating_person () : ",id(decorating_person))
        input_func() # calling original function i.e marriage_proposal_meeting()
    
    return decorating_person # returning decorating_person function type object referance.


def marriage_proposal_meeting(): # marriage_proposal_meeting() declared
    print("Showing a person as it is")

marriage_proposal_meeting = person_decorator(marriage_proposal_meeting)   # calling person_decorator() with function as argument
                                                                            # returning decorating_person function type object
                                                                            # and assigned to marriage_proposal_meeting # function aliasing happned.
marriage_proposal_meeting() # calling decorating_person() by its aliase name marriage_proposal_meeting

print("Memory location of marriage_proposal_meeting : ",id(marriage_proposal_meeting)) 

# o/p :
    # Memory location of person_decorator() :  2022000989600
    # Memory location of (input_func) original marriage_proposal_meeting() :  2022000987296
    # send person to beauty parlour
    # showing a person with full decoration
    # Memory location of decorating_person () :  2022000990032
    # Showing a person as it is
    # Memory location of marriage_proposal_meeting :  2022000990032

# decorating_person and marriage_proposal_meeting pointing to same function type object. i.e 2022000990032

#-----------------------------------------------------------------------------------------------------------

# example 2:

def add_decorator(func_input): # add = func_input # Aliasing happned
    def add_enhancement(x,y): # extending functionality # no. of argument must be same as add(a,b)
        print("*"*35)
        print("a is {2} and b is {1}, addition is {0}".format(x+y,y,x))
        print("*"*35)
        func_input(x,y) # calling original add(a,b) function.
    return add_enhancement # returning add_enhancement function type object

@add_decorator
def add(a,b):
    print(a+b)
    
add(10,20) # calling add_enhancement(x,y) with two argument 10 and 20

# o/p :
        # ***********************************
        # a is 10 and b is 20, addition is 30
        # ***********************************
        # 30

# note: if we remove @add_decorator then add(10,20) is a call to to original add(a,b) function.
        # in that case o/p will be 30 only
