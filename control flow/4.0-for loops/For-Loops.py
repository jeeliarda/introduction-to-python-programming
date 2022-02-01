'''For Loops

A for loop is used to "iterate", or do something repeatedly, over an iterable.
An iterable is an object that can return one of its elements at a time.
This can include sequence types, such as strings, lists, and tuples, as well as non-sequence types, such as dictionaries and files.
common pattern: the name of list cities is the plural form of city'''
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city.title())
print("Done!")

'''
output:
New York City
Mountain View
Chicago
Los Angeles
Done!
'''
'''Using the range() Function with for Loops
range() is a built-in function used to create an iterable sequence of numbers.
range(start=0, stop, step=1)'''
print(range(4))                 # range(0, 4)
print(list(range(4)))           # [0, 1, 2, 3]
print(list(range(2, 6)))        # [2, 3, 4, 5]
print(list(range(1, 10, 2)))    # [1, 3, 5, 7, 9]
'''we adopt range in a list before printing it, because printing just the output of range only shows you a range object
Creating and Modifying Lists
we can create a list by appending to a new list at each iteration'''

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

'''Modifying a list is a bit more involved, and requires the use of the range() function.'''

'''don't forget to add range()'''

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()



#----------------Quiz: For Loops

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    newName = name.replace(" ", "_").lower()
    usernames.append(newName)

print(usernames)

'''
output:
['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']
'''

'''str.replace(old, new[, count])
str.replace(old, new[, count])'''

'''Q2: Let's say instead of creating a new list, we want to modify the names list itself with the changes and write the following code. What would this do?'''

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)

'''answer	option	reason
Modifies the names list so that each name is lowercase and separated by underscores	
(X)	Causes a runtime error	
(O)	The printed output for the names list will look exactly like it did in the first line	It doesn't modify the contents of the names list at all. To modify the list you must operate on the list itself, using range, as you saw earlier.
Deletes the list	
Quiz: Tag Counter
Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.

You can assume that the list of strings will not contain empty strings.'''

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if (token.startswith('<') and token.endswith('>')):
        count += 1

print(count) # 2

'''if we don't want to use str.startswith() and str.endswith() method, we can use the method 2.'''

'''method 1:'''
'''if (token.startswith('<') and token.endswith('>')):'''

'''method 1:'''
'''if token[0] == '<' and token[-1] == '>':

str.startswith(prefix[, start[, end]])
str.startswith(prefix[, start[, end]])
str.endswith(suffix[, start[, end]])
str.endswith(suffix[, start[, end]])'''