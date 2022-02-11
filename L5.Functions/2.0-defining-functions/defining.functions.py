#-------Defining Functions
def cylinder_volumes(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volumes(10, 3) # function call statement
print(cylinder_volumes(10, 3))

'''
output:
282.7431
'''
'''Function Header
defining functions always starts with the def keyword and ends with colon(:)
following def is the name of the function cylinder_volumes
this needs one word with no gaps
the rules for function names are the same as those for variable names (snake case)
after the function name are parentheses that includes the arguments height and radius, separated by commas
argument: values passed in as input to a function
parameter vs. arguments
warning: the class doesn't clarify the differences between (formal) parameters and (actual) arguments, click here for more details
A parameter is a named variable passed into a function.
Parameter variables are used to import arguments into functions.'''

def cal_bmi(weight, height): # parameter = weight, height
    return weight / ((height/100)**2)

print(cal_bmi(50, 165)) # argument = 50, 165

'''
output:
18.36547291092746
'''
'''Function Body
the body of function is indented after the header and is where the function does its work
local variable: can only be used within the body of its function
variable scope: determines which variables you have access to
the body of function will often include return keyword, it's used to give back an output value when the function is called
Rather than returning the value as it is calculated, an alternative technique would be to calculate the value earlier and then store it in a variable
before

return height * pi * radius ** 2
after

volume = height * pi * radius ** 2
return volume
function_metaphor

functions like machines that take input (or arguments) and process them into ouput (or return values)
return_value = print("I wish to register a complaint.")

print("Output: ", return_value)'''

'''
output:
I wish to register a complaint.
Output:  None
'''
#This is a good image but it's incomplete

'''cuz some functions like print() don't return anything at all
print() displays text on the output window but don't return anything
None is when a function will return by default if it doesn't explicitly return anything else
diff between print() and return'''

'''print() provides output to the console while return provides the value
It's not necessary that every function has a return statement'''

def print_greeting():
    print('Hello World!')
#Default Arguments
def cylinder_volumes(height, radius = 5):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volumes(10, 5))  # 785.3975
print(cylinder_volumes(10))     # 785.3975

'''default arguments allow functions to use default values when those arguments are omitted
it's helpful because it can make code more concise in scenarios where there's common value we can use for a variable'''
print(cylinder_volumes(10, 7)) # 1539.371

'''arguments are still customizable, we are overriding the default value in the example below:
notice: we're passing values to our arguments by position
there're two way to pass values
by position
'''
print(cylinder_volumes(10, 7)) # by position

#by name

print(cylinder_volumes(height = 10, radius = 7)) # by name

print(cylinder_volumes(radius = 7, height = 10)) # it's also acceptable