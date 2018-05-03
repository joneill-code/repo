"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math
from math import log

def time_decorator(my_def):

    def internal_wrapper():

        t0 = time.time()
        def_result = my_def()
        t1 = time.time()
        print("{} finished in {} seconds".format(my_def.__name__, t1-t0))
        print("{} processed in {}".format(my_def.__name__, time.process_time()))
        print("{} is the size of the return value".format(sys.getsizeof(def_result)))
        return(def_result)

    return internal_wrapper

@time_decorator
def for_loop():
    alist = []
    for i in range(0, 1000000):
        alist.append(i)

    return alist
#print(type(for_loop()))
@time_decorator
def for_loop_log():
    alist = []
    for i in range(1,1000000):
        i = math.log(i)
        alist.append (i)

    return alist
#print(for_loop_log())
@time_decorator
def list_comp():
    return [i for i in range(0,1000000)]

@time_decorator
def list_comp_log():
    return [math.log(i) for i in range(1,1000000)]
@time_decorator
def numpy_list():
    return numpy.arange(1, 1000000)
print(numpy_list())

@time_decorator
def numpy_list_log():
    return numpy.log10(numpy.arange(1, 1000000))

@time_decorator
def pandas_list():
    return pandas.Series(1,[x for x in range(1000000)])
#print(pandas_list())

@time_decorator
def pandas_list_log():
    return pandas.Series(1,[math.log(x) for x in range(1,1000000)])
#print(pandas_list_log())

@time_decorator
def generator_list():
    return (x for x in range(100000))

@time_decorator
def generator_list_log():
    return (log(x) for x in range(1,100000))

