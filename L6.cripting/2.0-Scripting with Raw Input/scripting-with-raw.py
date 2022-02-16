'''input(): input a str
this is a demo with input()

name = input('Enter a name: ')
print('Hello', name.title())
now we input a name alan, it'll output the string Hello Alan

$ python3 input_demo.py
Enter a name: alan
Hello Alan
input(): input a int, float
if we want to input a integer...

num = input('Enter a number: ')
num += 20
print(num)
it'll show TypeError

$ python3 input_demo.py
Enter a number: 5
Traceback (most recent call last):
  File "tempCodeRunnerFile.python", line 2, in <module>
    num += 20
TypeError: can only concatenate str (not "int") to str
because we need to convert type into int by using method int()

num = int(input('Enter a number: '))
num += 20
print(num)
as long as we input a integer, the output will as our expected

$ python3 input_demo.py
Enter a number: 5
25
but if the input isn't integer, there's a ValueError

$ python3 input_demo.py
Enter a number: 4.5
Traceback (most recent call last):
File "tempCodeRunnerFile.python", line 1, in <module>
  num = int(input('Enter a number: '))
ValueError: invalid literal for int() with base 10: '4.5'
we need to convert type to float() just like this:

num = float(input('Enter a number: '))
num += 20
print(num)
output:

$ python3 input_demo.py
Enter a number: 4.5
24.5
but what if we need an integer, like multiplying a string by it to repeat it a certain number of times?

num = float(input('Enter a number: '))
print('hello' * num)
this wouldn't work even if we input an integer nubmer

$ python3 input_demo.py
Enter a number: 3
Traceback (most recent call last):
  File "tempCodeRunnerFile.python", line 2, in <module>
    print('hello' * num)
TypeError: can't multiply sequence by non-int of type 'float'
we can wrap float() within int() to convert to int

num = int(float(input('Enter a number: ')))
print('hello' * num)
that works

$ python3 input_demo.py
Enter a number: 3
hellohellohello
imagine and handle every possible case is important!

we'll learn a better way to handle these scenarios in the next section

eval()
here's another way we can interpret user input

eval(): a built-in function that evaluate a string as line in Python

x = eval(input('Enter an expression: '))
print(x)
output:

$ python3 input_demo.py
Enter an expression: 25 + 32
57
we can even include a variable like this:

num = 30
x = eval('num + 42')
print(x)
output:

$ python3 input_demo.py
72
L6-9. Quiz: Scripting with Raw Input
Quiz: Generate Messages
Imagine you're a teacher who needs to send a message to each of your students reminding them of their missing assignments and grade in the class. You have each of their names, number of missing assignments, and grades on a spreadsheet and just have to insert them into placeholders in this message you came up with:

Hi [insert student name],

This is a reminder that you have [insert number of missing assignments] assignments left to submit before you can graduate. Your current grade is [insert current grade] and can increase to [insert potential grade] if you submit all assignments before the due date.
You can just copy and paste this message to each student and manually insert the appropriate values each time, but instead you're going to write a program that does this for you.

Write a script that does the following:

Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades. Use this input to create lists for names, assignments, and grades.
Use a loop to print the message for each student with the correct values. The potential grade is simply the current grade added to two times the number of missing assignments.
my solution:

file: message.py

names = input('Enter names separated by commas: ').title().split(',') # get and process input for a list of names
assignments = input('Enter assignments count separated by commas: ').split(',') # get and process input for a list of the number of assignments
grades = input('Enter grade separated by commas: ').split(',') # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
note

we have to do .title() before .split(',')
the type of names is str before .split(','), otherwise is list
.split(','): separated by commas
zip(names, assignments, grades): it's useful to use zip() here
int(grade) + int(assignment)*2: we should convert assignment to int at first, otherwise it will repeats the string of assignment two times
input: message.input

chandler bing,phoebe buffay,monica geller,ross geller
3,6,0,2
81,77,92,88
output:

$ python3 message.py < message.input
Enter names separated by commas: Enter assignments count separated by commas: Enter grade separated by commas: Hi Chandler Bing,

This is a reminder that you have 3 assignments left to submit before you can graduate. You're current grade is 81 and can increase to 8
7 if you submit all assignments before the due date.


Hi Phoebe Buffay,

This is a reminder that you have 6 assignments left to submit before you can graduate. You're current grade is 77 and can increase to 8
9 if you submit all assignments before the due date.


Hi Monica Geller,

This is a reminder that you have 0 assignments left to submit before you can graduate. You're current grade is 92 and can increase to 9
2 if you submit all assignments before the due date.


Hi Ross Geller,

This is a reminder that you have 2 assignments left to submit before you can graduate. You're current grade is 88 and can increase to 92 if you submit all assignments before the due date.
note

we can input from file by using < filename'''