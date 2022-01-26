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

