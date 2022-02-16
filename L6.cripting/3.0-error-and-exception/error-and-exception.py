'''Errors and Exceptions
Errors
Syntax errors occur when Python can’t interpret our code, since we didn’t follow the correct syntax for Python.

These are errors you’re likely to get when you make a typo, or you’re first starting to learn Python.

file: errors_demo.py

msg = 'Welcome to this program!
print(msg)
output:

$ python3 errors_demo.py
  File "tempCodeRunnerFile.python", line 1
    msg = 'Welcome to this program!
                                  ^'''
'''SyntaxError: EOL while scanning string literal
Exceptions
Exceptions occur when unexpected things happen during execution of a program, even if the code is syntactically correct

There are different types of built-in exceptions in Python, and you can see which exception is thrown in the error message.

file: exceptions_demo1.py

x = int(input('Enter a number: '))
x += 20
print(x)
output:'''

'''$ python3 exceptions_demo1.py
Enter a number: ten
Traceback (most recent call last):
  File "exceptions_demo1.py", line 1, in <module>
    x = int(input('Enter a number: '))'''
'''ValueError: invalid literal for int() with base 10: 'ten'
ValueError occurs when a built-in operation or function is given an argument with the correct type but an inappropriate value
file: exceptions_demo2.py'''

'''print(nonexistent_variable)
output:'''

'''File "exceptions_demo2.py", line 1, in <module>
    print(nonexistent_variable)
NameError: name 'nonexistent_variable' is not defined
'''

'''Quiz: Errors and Exceptions
Q2: Here are some of the common exceptions programmers run into in Python. Do some research online to match the appropriate description for each.
'''
'''BUILT-IN EXCEPTION	DESCRIPTION
ValueError	An object of the correct type but inappropriate value is passed as input to a built-in operation or function.
AssertionError	An assert statement fails.
IndexError	A sequence subscript is out of range.
KeyError	A key can't be found in a dictionary.
TypeError	An object of an unsupported type is passed as input to an operation or function.'''