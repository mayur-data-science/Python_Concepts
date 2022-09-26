# FUNCTION ALIASING:
#        For existing function we can give another name this is nothing but function aliasing

# In python everything is treated as an object
# Even functions also internally treated as object only
# In python by default function name considered as referance variable name.
# proof: 

def add():
    print("hello world")

print(add) # <function add at 0x000001BD7778AF80>
# "add" is an referance variable which is pointing to "function" type object "at" so and so memory location.
print(id(add)) # 1913264844672 i.e Hexadecimal representation is 0x000001BD7778AF80
# In this(1913264844672 i.e 0x000001BD7778AF80) memory location, object of an function type is present.

# Can we create another referance variable for add() function?
# YES, why not, we can create another referance variable..
# ..which is pointing to same function type object which already add reference variable is pointing to.

add1 = add # what ever object pointed by add, for same object can you please assign add1 refrance variable also
print(add1) # <function add at 0x000001BD7778AF80>
print(id(add))  # 1913264844672 i.e Hexadecimal representation is 0x000001BD7778AF80
print(id(add1)) # 1913264844672 i.e Hexadecimal representation is 0x000001BD7778AF80
# now add1 referance variable also pointing to the same object which add is pointing to.
# This is called function aliasing.
add() # calling function add at 0x000001BD7778AF80 location.
# or you can also call like.
add1() # calling function add which is present at 0x000001BD7778AF80 memory location.

del add # deleted the add referance variable for function type object.
# this function type object is not available for garbage collection automatically because there is another ...
#...referance variable is assigned to it i.e "add1"
# we can access "add()" function by "add1" referance variable.
# add() # NameError: name 'add' is not defined.
add1() # happly called add() function.

# Q) what is the difference between below two line 
# 1) add1 = add   ---> add1 and add are pointing to same function object, its function aliasing
# 2) add1 = add() ---> we are calling add() function and whatever add() function returns we are assigning it to add1 variable.
#  print(add1) o/p: None   ---> in this example add() function returns "None" as default return value of function is "None".