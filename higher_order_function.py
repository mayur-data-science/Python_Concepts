# Higher Order Functions : (Passing Function's as an Argument's)

# Is it possible to pass a function as an arguments to another function???
#  ---> YES, we can pass a function as an arguments to another function.

# Functions that can accept other functions as arguments are also called higher-order functions. 

# Ex-->1 passing one function
def higher_order_function(func): # func = fx , internally function aliasing happned.
    print(" higher_order_function got {} function as an argument".format(func))
    
    func() # calling function fx() by it aliase name func 

def fx(): # function fx declared
    print("inside fx function")

def fy(): # function fy declared
    print("inside fy function")


higher_order_function(fx) # we are calling higher_order_function by passing fx function as an argument.

# o/p: higher_order_function got <function fx at 0x0000015047B895A0> function as an argument
#      inside fx function

# Ex-->2 passing multiple functions.

def higher_order_function(func1,func2): # func1 = fx , internally function aliasing happned. # accept two parameter.
                                        # func2 = fy , internally function aliasing happned.
    print(" higher_order_function got {},{} function's as an argument's".format(func1,func2))
    
    func1() # calling function fx() by it aliase name func1
    func2() # calling function fy() by it aliase name func2 

def fx(): # fx declared
    print("inside fx function")

def fy(): # fy declared
    print("inside fy function")


higher_order_function(fx,fy) # we are calling higher_order_function by passing fx and fy function's as an argument's.

# o/p : higher_order_function got <function fx at 0x000001F6AD5752D0>,<function fy at 0x000001F6AD575360> function's as an argument's
#       inside fx function
#       inside fy function
#-----------------------------------------------------------------------------------------------------------------------------------------

# Ex-->3 passing multiple functions with arguments.
def higher_order_function(func1,func2): # func1 = add , internally function aliasing happned. # accept two parameter.
                                        # func2 = sub , internally function aliasing happned.
    print("higher_order_function got {},{} function's as an argument's".format(func1,func2))
    
    func1(num1,num2) # calling function add() having positional arguments by it aliase name func1
    # func1() # TypeError: add() missing 2 required positional arguments: 'num1' and 'num2' 
    func2(num1,num2) # calling function sub() having positional arguments by it aliase name func2
    # func2() # TypeError: sub() missing 2 required positional arguments: 'num1' and 'num2'

num1 = int(input("Enter num1 : ")) # User input # global variable
num2 = int(input("Enter num2 : ")) # User input # global variable

def add(num1,num2): # add declared # accept two parameter.
    print("inside add function")
    print(num1+num2)

def sub(num1,num2): # sub declared # accept two parameter.
    print("inside sub function")
    print(num1-num2)


higher_order_function(add,sub) # we are calling higher_order_function by passing add and sub function's as an argument's.

#--------------------------------------------------------------------------------------------------------------------------------------

# Ex--->4 passing multiple functions with arguments (global variable concept)

def higher_order_function(func1,func2): # func1 = add , internally function aliasing happned.
                                        # func2 = sub , internally function aliasing happned.
    print("higher_order_function got {},{} function's as an argument's".format(func1,func2))
    
    func1(num1,num2) # calling function add() having positional arguments by it aliase name func1.
    # func1() # TypeError: add() missing 2 required positional arguments: 'num1' and 'num2'. 
    func2(num1,num2) # calling function sub() having positional arguments by it aliase name func2.
    # func2() # TypeError: sub() missing 2 required positional arguments: 'num1' and 'num2'.


num1 = int(input("Enter num1 : ")) # global variable num1.
num2 = int(input("Enter num2 : ")) # global variable num2.

def add(num1,num2): # add() function declared # accept two  parameter.
    print("inside add function")
    num1 = num1 + num2 # (not modifying global num1) creating local num1 variable [scope of num1 is within add() function].
    print("local num1 : ",num1) # printing local variable num1.
    

def sub(num1,num2): # sub() function declared # accept two parameter.
    print("inside sub function")
    num2 = num1 - num2 # (not modifying global num2) creating local num2 variable [scope of num2 is within sub() function].
    print("local num2 : ",num2) # printing local variable num2.

higher_order_function(add,sub) # we are calling higher_order_function by passing add and sub function's as an argument's.

print("global num1 : ",num1) # global variable unaffected
print("global num2 : ",num2) # global variable unaffected

# o/p : 
# Enter num1 : 10
# Enter num2 : 5
# higher_order_function got <function add at 0x000002AAC9278CA0>,<function sub at 0x000002AAC9279750> function's as an argument's
# inside add function
# local num1 :  15
# inside sub function
# local num2 :  5
# global num1 :  10
# global num2 :  5


# Ex--> 5
