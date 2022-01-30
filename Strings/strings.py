#we can define a string with either double quotes " or single quotes '

print("hello") # double quotes
print('hello') # single quotes
#although there're some edge cases, like having quotating mark in our string

#pet_halibut = "Why should I be tarred with the epithet "loony" merely because I have a pet halibut"

# SyntaxError: invalid syntax
#there're two solutions:

#place the string in single quotes rather than double quotes
pet_halibut = 'Why should I be tarred with the epithet "loony" merely because I have a pet halibut'
#use the backslash(\) to escape quotes (recommended)
#salesman = '"I think you\'re an encyclopaedia salesman'"
#there're few operations that used for int and float that we can also use for strings

#+: combine strings

#*: repeat strings

first_word = "Hello"
second_word = "There"
print(first_word + " " + second_word) # Hello There

word = "Hello"
print(word * 5) # HelloHelloHelloHelloHello

print(first_word / second_word) # TypeError: unsupported operand type(s) for /: 'str' and 'str'
len()
#len() is a built-in function that returns the length of an object
udacity_length = len("Udacity")
print(udacity_length) # 7


#----------exirice--------------

#Q5: We've just used the len function to find the length of strings. What does the len function return when we give it the integer 835 instead of a string?

#answer	option	reason
835	
3	
2	
#(O)	Error	
len(835) # TypeError: object of type 'int' has no len()

'''L2.16 Type and Type Conversion
there're specially designed functions for working with each data type
e.g. In L2.14 Quiz: Strings, len(835) returns an error, because it only accept string as a parameter
L2.17 Quiz: Type and Type Conversion
Quiz: Total Sales
In this quiz, you’ll need to change the types of the input and output data in order to get the result you want.

Calculate and print the total sales for the week from the data provided. Print out a string of the form "This week's total sales: xxx", where xxx will be the actual total of all the numbers. You’ll need to change the type of the input data in order to calculate that total.'''

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales) # don't forget convert back to str type
print("This week's total sales: " + weekly_sales)


#functions are similiar to operators
#the only difference is how they look
#diff	operator	function
#inputs placement	next to an operator	in the parentheses
#notation	short symbols	descriptive name
#there're three techniques for operating a value

#operator
function
#method
#Method: a function that belongs to an object

#methods are associated with specific types of objects
#that is, there are different methods depending on the type of date we're working with
#e.g. .title() only work with string type

print("sebastian thrun".title()) # Sebastian Thrun
#Argument(引數): the inputs in the parentheses

#the object is always the first argument to method
#e.g. "sebastian thrun" and full_name is the argument of title() and islower methods.
print("sebatian thrun".title())
full_name = "sebastian thrun"
print(full_name.islower())
#L2.20 String Methods
#format() Practice

#Use the coding space below to practice using the format() string method. There are no right or wrong answers here, just practice!

# Write two lines of code below, each assigning a value to a variable

ncu_students = 1
ccu_students = 2

# Now write a print statement using .format() to print out a sentence and the 
#   values of both of the variables

print("the student in 中字輩 is {0}".format(ncu_students + ccu_students))
#doc
str.format()
#L2.21 Another String Method - Split
#two arguments:
#sep: seperator
#if not specified or None, default is blank space
#it can consists of multiple character
#maxsplit: the list will have at most maxsplit + 1 elements
#if not specified or -1, then there's no limit
# if not given, default is blank space
new_str = "The cow jumped over the moon."
new_str.split() # ['The', 'cow', 'jumped', 'over', 'the', 'moon.']

# the list will have at most 3+1 = 4 elements
new_str.split(' ', 3) # ['The', 'cow', 'jumped', 'over the moon.']

# sep
new_str.split(None, 3) # ['The', 'cow', 'jumped', 'over the moon.']

# empty string will still be seperated
'1,,2'.split(',') # ['1', '', '2']

# sep can consists of multiple characters
'1<>2<>3'.split('<>') # ['1', '2', '3']
#tip: None is a type called NoneType

print(type(None)) # <class 'NoneType'>
#doc
str.split()
#L2.22 Quiz: String Methods Practice
#print the following question about the verse
#What is the length of the string variable verse?
#What is the index of the first occurrence of the word 'and' in verse?
#What is the index of the last occurrence of the word 'you' in verse?
#What is the count of occurrences of the word 'you' in the verse?
#You will need to refer to Python's string methods documentation.
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
message = "the length of the verse is {}, the index of the first occurrence of the word 'and' in verse is{}, the last occurrences of the word 'you' in verse {}, the count of occurrences of the word 'you' in verse is {}"

length = len(verse) # 362
first_idx = verse.find("and") # 65
last_idx = verse.rfind("you") # 186
count = verse.count("you") # 8

print(message.format(length, first_idx, last_idx, count))
#tip
#we can create an empty curly braces({}) at first, then add arguments later inside the format method.
#doc
str.find()
str.rfind()
str.count()