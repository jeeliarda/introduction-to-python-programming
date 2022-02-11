'''variable scope: the parts of program that a variable can be referenced, or used from
Local Variable
if a variable is created inside function, it can only be used within that function'''

def show_number():
    number = 10
    print(number) # 10

show_number()
print(number) # NameError: name 'number' is not defined

'''Global Variable
alternatively, we might have a variable defined outside of functions'''

number = 10

def show_number():
    print(number) # 10

show_number()
print(number) # 10

#the value of a global variable can NOT be moditfied inside the function, see L5-7. Quiz: Variable Scope for the details

'''More on Variable Scope
reusing names for objects is OK as long as you keep them in separate scope
good practice: define variables in the smallest scope they will be needed in
L5-7. Quiz: Variable Scope
Read through this code snippet:'''

egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()

#What is the result of running this code? If you aren't sure, try running it on your own computer!

'''answer	option
egg_count equals zero
egg_count equals 12
(O)	An error occurs
output:'''

#UnboundLocalError: local variable 'egg_count' referenced before assignment
#reason:

'''Python doesn't allow functions to modify variables that are outside the function's scope
A better way would be to pass the variable as an argument and reassign it outside the function
L5-8. Solution: Variable Scope
If we try to change or reassign global variable inside function, we get an error
Python doesn't allow functions to modify variables that aren't in the function's scope
A better way to write this would be:
pass the variable as an argument and reassign it outside the function'''

egg_count = 0

def buy_eggs(count):
    return count + 12 # don't modify global variable

egg_count = buy_eggs(egg_count)



'''Check for Understanding
It is important to understand variable scope, as this often can lead to confusion when writing code that solves complex problems.'''

EQ1
#Use the code below to determine what will print to the console.

str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()
#What will happen when we run this code?

'''answer	option	reason
(O)	It will print 'Variable scope is an important concept.'	we use the local variable rather than global variable
It will print 'Functions are important programming concepts.'	
(X)	It will give a ValueError.	
Q3
We made another tweak to the code.
'''
def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn(str1)

#What do you think what will happen when we run this code?

'''answer	option	reason
(O)	It will give a TypeError: print_fn() takes 0 positional arguments but 1 was given	
(X)	It will print 'Variable scope is an important concept.'	
It will print nothing.	
Q4
We made a final tweak to the code.'''

str1 = 'Functions are important programming concepts.'

def print_fn():
    print(str1)

print_fn(str1)

#Now what do you think will happen?

'''answer	option	reason
(O)	It still gives a TypeError: print_fn() takes 0 positional arguments but 1 was given	
(X)	It will print 'Functions are important programming concepts'	
It will not print anything.	
conclusion: As long as the function definition did not include any parameters, call function with arguments will give an error'''