'''Data Structure: containers that organize and group data types, which contain other data types and even other containers
List
a data type for mutable ordered sequences of elements
zero-based indexing
index start from 0
how far the element is from the beginning of the list
the last element index is -1'''

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(months[0]) # January
print(months[1]) # February
print(months[7]) # August

print(months[-1]) # December
print(months[-0]) # January

print(months[25]) # IndexError: list index out of range

'''lists can contain any mix and match of the data types'''

list_of_random_things = [1, 3,4, 'a string', True]

'''Slice and Dice with Lists
slicing: using indices to slice off parts of an object
lower bound is inclusive; upper bound is exclusive'''

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#q3 = month[6:9] # ['July', 'August', 'September']

#first_half = month[:6] # ['January', 'February', 'March', 'April', 'May', 'June']
#second_half = month[6:] # ['July', 'August', 'September', 'October', 'November', 'December']

'''lists are most similar to strings
both types support len function, indexing, and slicing
len(str) contains empty spaces'''

greeting = "Hello there"
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(len(greeting), len(months)) # 11 12
print(greeting[6:9], months[6:9]) # 'the' ['July', 'August', 'September']

#------------------Membership Operators

'''in: evaluates if object on left side is included in object on right side
not in: evaluates if object on left side is not included in object on right side
support both string and list type'''

greeting = "Hello there"
print('her' in greeting, 'her' not in greeting)
# True False

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print('Sunday' in months, 'Sunday' not in months)
# False True

#------------------Mutability and Order
'''Strings vs. Lists
Features	Strings	Lists
Support indexing	O	O
Support slicing	O	O
Support len()	O	O
Elements	sequences of letters	any type of objects
Mutability	X	O
Order	O	O'''

#--------Quiz: Lists and Membership Operators

'''Quiz: Slicing Lists
Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!'''
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
    'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
    'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
    'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[:-3]) # X
print(eclipse_dates[-3:]) # O, start from index of -3

