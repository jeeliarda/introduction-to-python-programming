#Handling Errors

'''Try Statement
Without Errors Handling
file: demo1.py
'''
#x = int(input('Enter a number: '))
#output

'''$ python3 demo1.py
Enter a number: nope
Traceback (most recent call last):
  File "demo1.py", line 1, in <module>
    x = int(input('Enter a number: '))
ValueError: invalid literal for int() with base 10: 'nope'
With Errors Handling
file: demo2.py'''

'''try:
    x = int(input('Enter a number: '))
except:
    print('That\'s not a valid number')

print('\nAttempted Input\n')'''

#output
'''

$ python3 demo2.py
Enter a number: nope
That's not a valid number

Attempted Input
Keep running until user input a valid number
file: demo3.py'''

'''while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number!')

    print('\nAttempted Input\n')'''
#output

'''$ python3 demo3.py
Enter a number: ten
That's not a valid number!

Attempted Input'''

'''Enter a number: hello
That's not a valid number!

Attempted Input

Enter a number: 10
Finally
finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.

the finally block is useful for cleaning up actions in the code.

later in this course, we will use finally to close file after attempting to open in a try statement.
file: demo4.py
'''
while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')

#output

'''$ python3 demo4.py
Enter a number: hello
That's not a valid number!

Attempted Input

Enter a number: hi
That's not a valid number!

Attempted Input

Enter a number: 10

Attempted Input

Specifying Exceptions
In the demo4.py, if we exit the program with Ctrl + C, it doesn't stop the program

because the expect handle any error, including the KeyboardInterrupt error
$ python3 demo4.py
Enter a number: ^CThat's not a valid number!

Attempted Input

Enter a number: 10

Attempted Input

we can specify which error we want to handle
'''
'''try:
    # some code
except ValueError:
    # some code
code: demo5.py

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')
output

$ python3 demo5.py
Enter a number: hello
That's not a valid number!

Attempted Input

Enter a number: ^C
Attempted Input

Traceback (most recent call last):
  File "demo5.py", line 3, in <module>
    x = int(input('Enter a number: '))
KeyboardInterrupt
KeyboardInterrupt Error wasn't handled, so this program crashed.

reminder: although the program crashed, this code in the finally block was still executed.

If we want this handler to address more than one type of exception, we can include a parenthesized tuple after the except with the exceptions.'''
'''
try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code
code: demo6.py

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except (ValueError, KeyboardInterrupt):
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')
output

$ python3 demo6.py
Enter a number: ten
That's not a valid number!

Attempted Input

Enter a number: ^CThat's not a valid number!

Attempted Input

Enter a number: 10

Attempted Input

we can also execute different blocks of code depending on the exception, you can have multiple except blocks.
'''
'''try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code
demo7.py

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('That\'s not a valid number!')
    except KeyboardInterrupt:
        print('\nNo input taken')
        break # don't forget to add break statement
    finally:
        print('\nAttempted Input\n')
output

$ python3 demo7.py
Enter a number: hello
That's not a valid number!

Attempted Input

Enter a number: ^C
No input taken

Attempted Input
'''