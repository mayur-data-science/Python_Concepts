#----------------#
# next() function:
#----------------#    
        
        # The next() function in python programming is used to get the next item from a collection of values.
        # The next() takes two values as arguments namely - iterator and default-value. 
        # The next() function returns the next element of the iterable object as output.
        
        # the next() function takes two arguments:
            # iterator: Iterator is an object that is used to iterate over an iterable specified object or collection of values.
            # default:  default value is returned from the next() function if the iterator is completed or exhausted.
                        # The default value also makes sure that the function should not raise any error.
        
        # Note: The first argument is required, but the second argument is optional.
        # The default value is optional
        
        # The exception raised by the next() function is called StopIteration exception.(see in Ex : 2.0)
        # When the end of an iterator is reached, and we try to access the next item, the python interpreter searches for the default value. 
        # If a default value is not given, then the program will raise an StopIteration error.
        
        # StopIteration is a built-in exception raised by the built-in function next() and an iterator's __next__() method,
        # which reminds that the iterator is exhausted or the iterator produces no further items.

# Ex : 0

random_list = ['A', 'B', 'C'] # initializing a list.

default_value = 'end' # setting a default value.


iterator_list = iter(random_list) # converting the list to an iterator.

next_element_1 = next(iterator_list, default_value)
print(next_element_1)

next_element_2 = next(iterator_list, default_value)
print(next_element_2)

next_element_3 = next(iterator_list, default_value)
print(next_element_3)

next_element_4 = next(iterator_list, default_value) # This will raise StopIteration Exception as the iterator is exhausted.
                                                    # but we used default value i.e 'end'
print(next_element_4)

    # o/p : 
        # A
        # B
        # C
        # end
            # The first three elements of the list are printed by the next() function, 
            # and when we tried to get the 4th or next element, it returned the default value.


#----------------------#
# Generators in python :
#----------------------#

        # Generator is a function which is responsible to generate a sequence of values.
        # We can write generator functions just like ordinary functions, 
        # but it uses yield keyword to return values.

        # Generators are pretty useful when working with sequences that allocate a large amount of memory.
        # Generators support an iteration protocol so when we call them, they do yield(produce) and (return) a data from a function and do not exit function.
        # its very opposite to normal functions where normal function return a data and exit.

        # when program cursor(the position indicator) comes to yield,
        # PVM automatically freez(Hold on to) the state of the function and provide data.
        # after providing(returning) the data, if data is asked again from same generator object, then,
        # that same generator object will resume its execution state and execute next line of code if any.

        # The advantage is that instead of having to compute the entire sequence at once, 
        # generators compute one value at a time and wait until the next value is called or asked for.

# Ex : 1

        # The range function is used for iterating over a range of values determined by the given start, stop, and step size.
# Ex : 1.1
print(range(5)) # o/p : range(0, 5)
                # If you execute the range function, you will not get any value returned.
# Ex : 1.2
for i in range(5):  # However, we can iterate over it in a for loop to access the values in order. 
                    # To provide the flow of numbers in a sequence, the range function keeps track of the last number and the step size.
    print(i)
    
    # o/p: 
            # 0
            # 1
            # 2
            # 3
            # 4


# Ex : 1.3

        # We can also view the entire sequence by converting a generator to a list.
print(list(range(0,5))) # o/p : [0, 1, 2, 3, 4]


# Ex : 2.0

    # We can create our own generator functions.
    # The syntax is quite similar to creating a normal function but there is a critical difference.
    
    # The main difference between a generator and a normal function is that we do not use the return keyword.
    # Instead, the yield keyword is used.

def mygen():
    yield 'A'
    yield "B"
    yield "C"

g = mygen()

    # We can iterate over a generator manually by using the next function.
print(next(g))  # A
print(next(g))  # B
print(next(g))  # C
print(next(g))  # StopIteration (we can also use default value to avoid Error )
    # If we call the next function on the generator after we reach the end, it will return a StopIteration error.
    
    # The for loop does the same steps as we do with the next() function.
    # However, we do not get a StopIteration error when using a for loop because it automatically catches this error.


# Ex : 2.1

def firstn(num):
    n=1
    while n<=num:
        yield n 
        n=n+1

values1 = firstn(5)

for x in values1:
    print(x)

list1 = list(values1) # when above for loop compelets values1 generator object exhausted(completely used up) 
print(list1) # o/p: []

values2 = firstn(5) # thats why we need to call firstn(num) generator function again. 
                    
list1 = list(values2)
print(list1) 


# Ex : 2.3
def mygenerator(n):
    for i in range(1, n, 2):
        yield i**3

for i in mygenerator(10):
    print(i)                # 1
                            # 27
                            # 125
                            # 343
                            # 729


for i in mygenerator(10):
    print(i)				# 1
                            # 27
                            # 125
                            # 343
                            # 729

print(next(mygenerator(10))) # 1
print(next(mygenerator(10))) # 1




# Ex : 3 (Python Generator Expression)

    # Another way to create a generator is by using a generator expression.
    # Similar to a lambda function, which creates anonymous functions, generator expressions create anonymous generator functions.
    # The syntax for generator expression is similar to that of a list comprehension in Python, except you use round parenthesis () instead of squared brackets [].
    
    # While the list comprehension produces the entire list all at once, 
    # the generator returns every number one at a time. This is called lazy execution.
    # This makes generator highly memory efficient than a list comprehension.

# Ex : 3.1

my_list = [i**3 for i in range(1,10,2)] # list comprehension produces the entire list all at once
print(my_list) # o/p : [1, 27, 125, 343, 729]
print(type(my_list)) # o/p : <class 'list'>


# Ex : 3.2

my_generator = (i**3 for i in range(1,10,2)) # generator expression, the generator returns every number one at a time if asked. 

print(type(my_generator)) # <class 'generator'>

print(next(my_generator)) # 1

for i in my_generator:
    print(i)            # 27
                        # 125
                        # 343
                        # 729

# for i in my_generator: 	# It is important to note that once we iterate over a generator and reach the end, we can not iterate over it again.
    #print(i)           	# For example, if we try to use my_generator again in our program nothing will be returned
                            # mygenerator is exhausted(completely used up) # no values to iterate over


print(next(my_generator))	# StopIteration (Error)

            # This is not the case in example 2.3 because we had a generator function which creates a generator each time it is executed. 
            # You may notice that we do not have a function call in this example. 
            # Instead, we have a generator object.






# Ex : 4

        # We often see the terms iterable and iterator. 
        # An iterable is an object that we can iterate over such as lists, sets, strings, and so on.
        #  However, we cannot take iterable objects as iterators.
        
        # There is a built-in Python function that converts an iterable to an iterator.
        # Surprisingly, it is the iter function.
        # For instance, we can iterate over strings but cannot use them as iterators.
        # The iter function allows using strings as iterators. 
        
        # my_string = "Python"
        # next(my_string) # TypeError: 'str' object is not an iterator

        # Let’s convert it to an iterator and then call the next function again.

my_string = "Python"

my_string_new = iter(my_string)
print(type(my_string_new)) # <class 'str_iterator'>

print(next(my_string_new)) # P
print(next(my_string_new)) # y
print(next(my_string_new)) # t

# Ex : 5 
        # The iter function can also be used to convert a list to an iterator.

my_list = ['a', 'b', 'c', 'd', 'e']
my_iter = iter(my_list)
print(type(my_iter)) # <class 'list_iterator'>

    # Let’s use it in a for loop.
for i in my_iter:
    print(i)    # o/p : # a
                        # b
                        # c
                        # d
                        # e

#-----------------------------------#
# Advantages of Generator Functions:#
#-----------------------------------#

            # 1) When compared with Class Level Iterators, Generators are very easy to use. 
            # 2) Improves Memory Utilization and Performance. 
            # 3) Generators are best suitable for reading Data from Large Number of Large Files. 
            # 4) Generators work great for web scraping and crawling.

#---------------------------------------------------------------#
# Generators vs Normal Collections with respect to Performance: #
#---------------------------------------------------------------#

import random
import time


names = ["mayur","priya","ranjeet","gaurav","rushi"]
subjects = ["python","java","blockchain"]


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            "id" : i,
            "name" : random.choice(names),
            "subject" : random.choice(subjects)
        }
        result.append(person)
    return result



def people_generator(num_people):
    for i in range(num_people):
        person = {
            "id" : i,
            "name" : random.choice(names),
            "subject" : random.choice(subjects)
        }
    yield person


t1 = time.time()
people = people_list(100000) 
t2 = time.time()
print('Took {}'.format(t2 - t1)) # Took 0.31189656257629395

t3 = time.time()
people = people_generator(1000000000000000000000000000000000000000) 
t4 =  time.time() 
print('Took {}'.format(t3 - t4)) # Took -0.010064363479614258

    # Note: In the above program observe the differnce wrt execution time by using list and Generators



#----------------------------------------------------------#
# Generators vs Normal Collections wrt Memory Utilization: #
#----------------------------------------------------------#


# Normal Collection:
# l=[x*x for x in range(10000000000000000)] 
# print(l[0])

    # We will get MemoryError in this case because all these values are required to store in the memory

# Generators:
g=(x*x for x in range(10000000000000000))
print(next(g))  # o/p : 0
print(next(g))  # o/p : 1
print(next(g))  # o/p : 4
print(next(g))  # o/p : 9

    # We won't get any MemoryError because the values won't be stored at the beginning


#--------------------------------------------------------------------------------------------------------#



# Ex : 1
def countdown(num):
    print("Start Countdown")
    while(num>0):
        yield num
        num = num-1

values = countdown(5)

for x in values:
    print(x)

    # o/p :
        # Start Countdown
        # 5
        # 4
        # 3
        # 2
        # 1


# Ex : 2 (To generate first n numbers)

def first_n(num):
    n = 1
    while n<=num :
        yield n
        n = n+1

values1 = first_n(5) # here PVM will not calling generater function

for x in values1:   # when PVM sees we asked data from generator function object, PVM will invoke generator first_n(num) function
                    # for x in values1 means we are asking current state data which is present in generator object to store in x.
                    # suppose we never asked for data present in generator object then than that function will never be invoked.
    print(x)

    # o/p : 
        # 1
        # 2
        # 3
        # 4
        # 5

# Ex : 3
    # To generate Fibonacci Numbers... (till 100)
    # The next is the sum of previous 2 numbers

def fibonacchi():
    previous_num, next_num = 1,2 #2

    while True: #3 #9 #15 #21 #27 #33 #39 #45 #51 #57 #63
        yield previous_num #4 #10 #16 #22 #28 #34 #40 #46 #52 #58 #64
        previous_num, next_num = next_num, previous_num + next_num #8 #14 #20 #26 #32 #38 #44 #50 #56 #62

for f in fibonacchi(): #1 #5 #11 #17 #23 #29 #35 #41 #47 #53 #59 #65
    if f>100: #6 #12 #18 #24 #30 #36 #42 #48 #54 #60 #66(144>100)(True)
        break #67
    print(f) #7 #13 #19 #25 #31 #37 #43 #49 #55 #61

        # Execution of program (#1 to #67)
        
        # when program cursor(the position indicator) comes to (#4 #10 #16 #22 #28 #34 #40 #46 #52 #58 #64),
        # PVM automatically pause the state(#4 #10 #16 #22 #28 #34 #40 #46 #52 #58 #64) of the function and provide data.
        # after providing(returning) the data, if data is asked (#1 #5 #11 #17 #23 #29 #35 #41 #47 #53 #59 #65) again from same generator object then,
        # that same generator object will resume its execution state and execute next line of code (#8 #14 #20 #26 #32 #38 #44 #50 #56 #62).

    # o/p : 
        # 1
        # 2
        # 3
        # 5
        # 8
        # 13
        # 21
        # 34
        # 55
        # 89

#-------------------------------------------------------------------------------------------#

import os
import psutil

number = 10000000


def memory_usage_in_MB(process):
  return  process.memory_info()[0] / float(2 ** 20)

process = psutil.Process(os.getpid())

memory1 = memory_usage_in_MB(process)
print("Memory before generator : ",memory1)

toto = (x*x for x in range(number))
tata = (x+x for x in toto)
tutu = (x-1 for x in tata)

memory2 = memory_usage_in_MB(process)

print("Memory after generator : ",memory2)
print("memory utilized by generator data: " + str(memory2 - memory1) + "MB")

memory1 = memory_usage_in_MB(process)
print("Memory before iterator : ",memory1)

toto = [x*x for x in range(number)]
toto = [x+x for x in toto]
toto = [x-1 for x in toto]

memory2 = memory_usage_in_MB(process)

print("Memory after iterator : ",memory2)
print("memory utilized by iterator data: " + str(memory2 - memory1) + "MB")

        # o/p :
            # Memory before generator :  16.9375
            # Memory after generator :  16.9375
            # memory utilized by generator data: 0.0MB
            # Memory before iterator :  16.94140625
            # Memory after iterator :  404.50390625
            # memory utilized by iterator data: 387.5625MB


#--------------------------------------------------------------------------#
# What is the difference between a normal function and a generator function?
#--------------------------------------------------------------------------#

    # The difference between a normal function and a generator function is that while a return statement terminates a function, 
    # yield statement will pause the function, save its current state and later continue from there in the next call.