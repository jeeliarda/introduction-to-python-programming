'''In Python, we can create lists really quickly and concisely with list comprehensions.
list comprehensions allow us to create a list using a for loop in one step.
list comprehensions are not found in other languages, but are very common in Python
without list comprehensions:'''

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

#with list comprehensions:

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

capitalized_cities = [city.title() for city in cities]

print(capitalized_cities) # ['New York City', 'Mountain View', 'Chicago', 'Los Angeles']

'''Add If
another example without list comprehensions:
'''
squares = []

for x in range(9):
    squares.append(x**2)

#another example with list comprehensions:

squares = [x**2 for x in range(9)] # [0, 1, 4, 9, 16, 25, 36, 49, 64]

#we can also add conditionals to list comprehensions

#add conditionals before ]

squares = [x**2 for x in range(9) if x%2 == 0] # [0, 4, 16, 36, 64]
#Add Else
#if we want to add an else, we will get an syntax error like this:

#squares = [x**2 for x in range(9) if x%2 == 0 else x+3] # SyntaxError: invalid syntax

#we have to move the conditionals at the beginning of the list comprehensions, right after the expression (x**2):

squares = [x**2 if x%2 == 0 else x+3 for x in range(9)] # [0, 4, 4, 6, 16, 8, 36, 10, 64]

#---------------Quiz: List Comprehensions
'''Quiz: Extract First Names
Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.'''

#don't forget to add [0]

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower().split(" ")[0] for name in names]
print(first_names)

'''
output:
['rick', 'morty', 'summer', 'jerry', 'beth']
'''
'''Quiz: Multiples of Three
Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
'''
#my solution:

multiples_3 = [x for x in range(1, 61, 1) if x%3 == 0]
print(multiples_3)

'''
output:
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
'''
#answer:

multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

'''
output:
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
'''
'''Quiz: Filter Names by Scores
Use a list comprehension to create a list of names passed that only include those that scored at least 65.'''

#don't forget to use .items() method when use for...in loop in dictionaries
scores = {
            "Rick Sanchez": 70,
            "Morty Smith": 35,
            "Summer Smith": 82,
            "Jerry Smith": 23,
            "Beth Smith": 98
        }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
#-----------Practice Questions
'''Question 1
we have the same variable nominated, winners:
click here to see the variables
1A. Create a dictionary that includes the count of Oscar nominations for each director in the nominations list'''

### 1A: Create dictionary with the count of Oscar nominations for each director
nom_count_dict = {}

for directors in nominated.values():
    for director in directors:
        if not nom_count_dict.get(director, None):
            nom_count_dict[director] = 1
        else:
            nom_count_dict[director] += 1

print("nom_count_dict = {}\n".format(nom_count_dict))

'''1B. Provide a dictionary with the count of Oscar wins for each director in the winners list.

warning: there's not only one winner a year sometimes
1961: ['Jerome Robbins', 'Robert Wise']
method 1: use the same approach as Q1A:

instead of using .items retrive both keys and values, we can use .keys() or .values() method alternatively'''

### 1B: Create dictionary with the count of Oscar wins for each director
win_count_dict = {}

for winner_list in winners.values():
    for winner in winner_list: # there's not only one winner a year sometimes
        if not win_count_dict.get(winner, None):
            win_count_dict[winner] = 1
        else:
            win_count_dict[winner] += 1

print("win_count_dict = {}".format(win_count_dict))
#method 2: if the directors aren't in the win_count_dict, get return 0 for the director

#before
if not win_count_dict.get(winner, None):
    win_count_dict[winner] = 1
else:
    win_count_dict[winner] += 1
#after
win_count_dict[winner] = win_count_dict.get(winner, 0) + 1
#Question 2
#Provide a list with the name(s) of the director(s) with the most Oscar wins. We are asking for a list because there could be more than 1 director tied for the most Oscar wins.

#the winners dictionary is same as above, I don't mention it again

#first shot:

### For Question 2: Please provide a list with the name(s) of the director(s) with
### the most Oscar wins. The list can hold the names of multiple directors,
### since there can be more than 1 director tied with the most Oscar wins.

most_win_director = []
# Add your code here
win_count_dict = {}

for winner_list in winners.values():
    for winner in winner_list:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1

win_name = [name for name in win_count_dict.keys()]
win_count = [count for count in win_count_dict.values()]
most_win_index = [index for index, count in enumerate(win_count) if count == max(win_count)]
most_win_director = [win_name[index] for index in most_win_index]

print("most_win_director = {}".format(most_win_director))

'''
output:
most_win_director = ['John Ford']
'''
#second shot:

#most_win_index can be wrote shorter

before

win_name = [name for name in win_count_dict.keys()]
win_count = [count for count in win_count_dict.values()]
most_win_index = [index for index, count in enumerate(win_count) if count == max(win_count)]

#after (if there's more than 1 most_win_index, the code below will only show the first match index)

most_win_index = max(win_count_dict.values())
#we don't need an win_name list to store all the winners. Just using list comprehensions instead.

#before

win_name = [name for name in win_count_dict.keys()]

most_win_director = [win_name[index] for index in most_win_index]
#after

most_win_director = [name for name, count in win_count_dict.items() if count == most_win_index]
#full code:

most_win_director = []
# Add your code here
win_count_dict = {}

for winner_list in winners.values():
    for winner in winner_list:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1

# most_win_index = max(win_count_dict.values())
most_win_index = [index for index, count in enumerate(win_count) if count == max(win_count)]
most_win_director = [name for name, count in win_count_dict.items() if count == most_win_index]

print("most_win_director = {}".format(most_win_director))

'''
output:
most_win_director = ['John Ford']
'''