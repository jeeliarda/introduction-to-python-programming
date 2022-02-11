'''set is a simple data structure, they have one main use: collecting unique elements
dictionary is more flexible
Dictionary
Dictionary: a data type for mutable objects that store mappings of unique keys to values(unordered)'''

'''dictionary stores pairs of elements, keys and values'''

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(elements['carbon']) # 6

'''we're adding lithium and giving it a value of three'''

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
elements['lithium'] = 3
print(elements) # {'hydrogen': 1, 'helium': 2, 'carbon': 6, 'lithium': 3}

'''dictionary keys are similar to list indices, but dictionary can have keys of any immutable type, not just integers'''

'''it's not necessary for every key to have the same type
dictionary also support in operator'''

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print('mithril' in elements) # False

'''get(): look up a value in a dictionary'''

'''it's recommended to use get() rather than dictionary[key], because the later will product an error, that can crash program'''

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(elements.get('hydrogen')) # 1
print(elements.get('delithium')) # None
print(elements['delithium']) # KeyError: 'delithium'

'''keys() and values: return a list of all the keys/values in the dictionary'''

'''look at the last line, it's sorted by the values(county name), not by the keys(rank)'''

jp_population_rank = {'3': 'osaka', '1': 'tokyo', '2': 'kanagawa'}

print(jp_population_rank.keys()) # dict_keys(['3', '1', '2'])
print(jp_population_rank.values()) # dict_values(['osaka', 'tokyo', 'kanagawa'])
print(sorted(jp_population_rank.keys())) # ['1', '2', '3']
print(sorted(jp_population_rank.values())) # ['kanagawa', 'osaka', 'tokyo']

'''we can check if a key return none with is operator, or the opposite is not operator'''

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}

x = elements.get('delithium') # None
is_null = x is None
not_null = x is not None
print(is_null) # True
print(not_null) # False

#------------------QUIZ

'''Quiz: Dictionaries and Identity Operators
Q2: Which of these could be used as the key for a dictionary? (Choose all that apply.) Hint: Dictionary keys must be immutable, that is, they must be of a type that is not modifiable.'''

'''answer	option	reason
(O)	str	
list	lists can be changed by adding and removing elements, they are mutable.
(O)	int	
(O)	float	
get with a Default Value
get() returns None (or a default value) if the key isn't found'''

'''In the last example, we specify the string "There's no such lement" instead of the default None'''
elements.get('dilithium') # None
elements['dilithium'] # KeyError: 'dilithium'
elements.get('kryptonite', 'There\'s no such   lement!') # "There's no such element!"

'''Checking for Equality vs. Identity: == vs. is'''
'''equality: =='''
'''identity: is'''
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b) # True
print(a is b) # True
print(a == c) # True
print(a is c) # False
'''expression	output	reason

a == b	True	List a and list b are equal(==) and identical(is)
a is b	True	as above
a == c	True	List c is equal(==) to a (and b) since they have same concpet
a is c	False	List b and list c are point to two different objects (i.e., they're not identical object)
L3-18. Check for Understanding: Data Structures'''

'''Q1: Which of the following statements about tuples are true? Select all that apply.

answer	option	reason
A tuple is a mutable data structure.	
(O)	A tuple is an ordered data structure.	
(O)	A tuple can be indexed and sliced like a list.	Tuple Support Indexing and Slicing
A tuple is defined by listing a sequence of elements separated by commas and contained within curly braces: {}	not {}, is ()'''

'''Q2: Which of the following statements about sets are true? Select all that apply.

answer	option	reason
(O)	A set is a mutable data structure.	we can modify the elements in a set with methods like add and pop.
A set is an ordered data structure.	A set is an unordered data structure, so you can't index and slice elements like a list; there is no sequence of positions to index with!
A set can be indexed and sliced like a list.	as above
(O)	A set does not contain duplicate elements.	
Q3: Is the following statement true or false? A set is the only data structure defined with curly braces: {}'''

'''answer	option	reason
True	
(O)	False	Set isn't the only data structure defined with curly braces, {}; dictionaries does as well'''
a = {}
print(type(a)) # <class 'dict'>

b = set()
print(type(b)) # <class 'set'>
c = dict()
print(type(c)) # <class 'dict'>

'''If you define a variable with an empty set of curly braces like this: a = {}, Python will assign an empty dictionary to that variable.
You can always use set() and dict() to define empty sets and dictionaries as well.'''

# invalid dictionary - this should break
room_numbers = {
    ['Freddie', 'Jen']: 403,
    ['Ned', 'Keith']: 391,
    ['Kristin', 'Jazzmyne']: 411,
    ['Eugene', 'Zach']: 395
}

# TypeError: unhashable type: 'list'

'''Q6: What's wrong with the code above?'''

'''answer	option	reason
The dictionary can not use a container for its keys	
(O)	The dictionary is using a mutable datatype for its keys	The lists used in the code above are NOT immutable, and thus cannot be hashed
There are too many values in each dictionary key	
In Python, any immutable object (such as an integer, boolean, string, tuple) is hashable

meaning its value does not change during its lifetime.
This allows Python to create a unique hash value to identify it
which can be used by dictionaries to track unique keys and sets to track unique values.
The code above would be fixed with a set data structure'''

# invalid dictionary - this should break
room_numbers = {
    ('Freddie', 'Jen'): 403,
    ('Ned', 'Keith'): 391,
    ('Kristin', 'Jazzmyne'): 411,
    ('Eugene', 'Zach'): 395
}

print(room_numbers[('Eugene', 'Zach')]) # 395