# In python everything is treated as an object
# Even functions also internally treated as object only
# proof: 

def add():
    print("hello world")

print(add) # <function add at 0x000002192AE2AEF0>
# "add" is an referance variable which is pointing to "function" type object "at" so and so location.
print(id(add)) # 2307116936944
# on this(0x000002192AE2AEF0) location id(2307116936944) is located.