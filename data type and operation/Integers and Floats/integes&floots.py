#Integers and Floats
#In python, every object we encounter will have a type
#int for integer values

#float for decimal or floating point values

print(3 / 4) # 0.75 is float
print(16 / 4) # 4.0 is still float

#type(): built-in function that returns the type of an object.

#if we add . after a whole number, that type will be float

type(387) # int
type(387.) # float
#a operation involving an int and float always produces a float

print(3 + 2.5) # 5.5
#we can use int() to manually convert type, it will cut the number after decimal point (not round off)

int(49.7) # 49
int(-49.7) # -49
#using float() convert int to float adds decimal zeros to the end of the number

float(3520 + 3239) # 6759.0

#floating numbers are approximations

#this tradeoff can sometimes have surprising results

print(0.1 + 0.1 + 0.1) # 0.30000000000000004
#Python Best Practices
#when calling a function, put opening parentheses after the name of the function

print(8)    # O
print (8)   # X
#don't put extra spaces immediately inside the parentheses either

print(3 * 7)    # O
print( 3 * 7 )  # X
#mixing operators with different priorities (like multiplication and subtraction), add space around the lower priority

print(3*7 - 1)      # O
print(3 * 7 - 1)    # X


#on't write extremely long lines of code, people commonly limit lines that are 79 or 99 characters long
#if we have to write longer lines, consider rewriting, simplifying, or separating code into multiple lines
#PEP8
#Python Developer's Guide
#purpose:
#clarity, make code easier to read
#consistency


#---------------Exercise Integers and Floats-----------------

#Divide by Zero
print(5/0)

'''
Traceback (most recent call last):
    File "/tmp/vmuser_kvvlefczqi/quiz.py", line 1, in <module>
    print(5/0)

ZeroDivisionError: division by zero
'''
#Traceback: What was the programming doing when it broke, this part is usually less helpful
#Error message is more helpful
#Two Types of Error
#In general, there are two types of errors to look out for
#Syntax: problem detected when Python checks the code before runs it
#Exceptions: problem that occurs when the code is running



#Booleans, Comparison Operators, and Logical Operators
#it's named for its inventor George Bool

#Boolean: holds one of the values True(1) or False(0)

the_sun_is_up = True
the_sun_is_down = False

