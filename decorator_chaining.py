# Decorator Chaining:

def func_A(input_function):

    def wraper_of_A(): # call from 7
        print("inside wrap of func_A") #8
        print(1) #9
        return input_function() #10 # calling wraper_of_C()

    return wraper_of_A


def func_B(input_function):

    def wraper_of_B(): #call from 4
        print("inside wrap of func_B") #5
        print(2) #6
        return input_function() #7 # calling wraper_of_A()

    return wraper_of_B


def func_C(input_function):

    def wraper_of_C(): # call from 10
        print("inside wrap of func_C") #11
        print(3) #12
        return input_function() #13 # Calling main()

    return wraper_of_C


@func_B #3 	# input_function for func_B(input_function) is wraper_of_A
            # returning wraper_of_B and automatically creating main referance variable(name same as original function name)
            # and assigning wraper_of_B to main
        
@func_A #2 	# input_function for func_A(input_function) is wraper_of_C
@func_C #1 	# input_function for func_C(input_function) is main
def main():
    print('Function') #14

main()#4 # calling main() is nothing but calling wraper_of_B()

# o/p :
        # inside wrap of func_B
        # 2
        # inside wrap of func_A
        # 1
        # inside wrap of func_C
        # 3
        # Function