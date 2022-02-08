'''We can use lambda expressions to create anonymous functions.
That is, functions that don’t have a name.
helpful for creating quick functions that aren’t needed later in your code.
higher-order functions: functions that take in other functions as arguments, where lambda expressions become especially useful
standard function vs. lambda expression'''

# standard function
def double(x):
  return x * 2

# lambda expression
double = lambda x: x * 2

#structure

'''lambda keyword: used to indicate that this is a lambda expression
x: (one or more) arguments
:
x * 2: expression that is evaluated and returned in this function
lambda functions aren't ideal for complex function, but it's useful for short symbol functions'''

#add commas(,) to use more than 1 argument

lambda x, y: x * y
'''Quiz: Lambda Expressions
Quiz: Lambda with Map
map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. The code below uses map() to find the mean of each list in numbers to create the list averages. Give it a test run to see what happens.'''

#Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().

#my solution:

numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]

# def mean(num_list):
#     return sum(num_list) / len(num_list)
mean = lambda num_list: sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

#answer:

'''we don't need a separate mean variable
using the short variable name like x
averages = list(map(lambda x: sum(x) / len(x), numbers))
Quiz: Lambda with Filter
filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True. The code below uses filter() to get the names in cities that are fewer than 10 characters long to create the list short_cities. Give it a test run to see what happens.'''

#Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter().

#my solution:

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

# def is_short(name):
#     return len(name) < 10
is_short = lambda name: len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)
#answer:

'''just like the example above, we don't need is_short variable
using the short variable name like x'''
short_cities = list(filter(lambda x: len(x) < 10, cities))