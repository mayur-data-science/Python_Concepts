#----------------------#
# Generators in python :
#----------------------#

        # Generator is a function which is responsible to generate a sequence of values.
        # We can write generator functions just like ordinary functions, 
        # but it uses yield keyword to return values.
        
        # Generators are pretty useful when working with sequences that allocate a large amount of memory.
        # Generators support an iteration protocol so when we call them, they do not return a value and exit like normal functions,
        # but they do yield a value and do not exit
        
        # After the next value in the sequence is generated,
        # they automatically suspend and resume their execution state at the last point when the next value is asked for.
        
        # The advantage is that instead of having to compute the entire sequence at once, 
        # generators compute one value at a time and wait until the next value is called for.

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
print(next(g))  # StopIteration
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

# Ex : 3
    # Another way to create a generator is by using a generator expression. It is similar to a list comprehension.

mygenerator = (i**3 for i in range(1,10,2)) # generator expression

print(next(mygenerator)) # 1

for i in mygenerator:
    print(i)            # 27
                        # 125
                        # 343
                        # 729

# for i in mygenerator: 	# It is important to note that once we iterate over a generator and reach the end, we can not iterate over it again.
    #print(i)           	# For example, if we try to use mygenerator again in our program nothing will be returned
                            # mygenerator is exhausted(completely used up) # no values to iterate over


print(next(mygenerator))	# StopIteration (Error)

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
my_gen = iter(my_list)
print(type(my_gen)) # <class 'list_iterator'>

    # Let’s use it in a for loop.
for i in my_gen:
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