'''Third-Party Libraries
Third-Party Libraries
pip: package manager that is included in Python 3

One popular alternative is Anaconda which is designed specifically for data science.

pip install sytax:

pip install package_name
Using a requirements.txt File
we used to list all the dependencies in a file called requirements.txt, make it easier to share

this's an example of requirements.txt:

there're 2 equal sign(=), not 1
version number is optional, but it usually should be included
beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1
we can use pip to install all dependencies from requirements.txt at once:

r for requirement
pip install -r requirements.txt
Useful Third-Party Packages
IPython - A better interactive Python interpreter
requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
Flask - a lightweight framework for making web applications and APIs.
Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
pytest - extends Python's builtin assertions and unittest module.
PyYAML - For reading and writing YAML files.
NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
ggplot - Another 2D plotting library, based on R's ggplot2 library.
Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
pyglet - A cross-platform application framework intended for game development.
Pygame - A set of Python modules designed for writing games.
pytz - World Timezone Definitions for Python'''


# Experimenting with an Interpreter
'''Experimenting With An Interpreter
type python or python3 in terminal will start a python interactive interpreter

python for v2.x, python3 for v3.x
it's an awesome place to experiment and try bits of python code
the value of the last line in a prompt will be outputted automatically

if having multiple lines, we still have to use print()
>>> type(5.23)
<class 'float'>
if we define a function, we will see a change at the left side(...), meaning continuation lines

we have to include our own indentation
>>> def cylinder_volume(height, radius):
...         pi = 3.14159
...         return height * pi * radius ** 2
A drawback of using interpreter is hard to edit code, we have to move cursor only by using keyboard, not mouse

to quit the Python interpreter

type exit() or hit Ctrl + D on macOS or Linux
type exit() or hit Ctrl + Z then Enter on Windows
IPython
It's an awesome alternative for default Python interpreter
It comes with many handy features:
tab completion
? for details about an object
! to execute system shell commands
syntax highlighting
and more'''

# Online Resources
'''Getting the information you need to know
(X) carry an encyclopedia's worth of knowledge in their heads
(O) finding information quickly
How to Search
using python or the name of the library
writing good search query can take multiple attempts, try again
try using keywords found on the page we found
copy and paste error messages, remove the unnecessary parts (e.g. line numbers that has error)
ask it ourself! Community like stackoverflow is a great place, but there's a etiquitte rules we have to follow
Hierarchy of Online Resources
While there are many online resources about programming, not all of the them are created equal. This list of resources is in approximate order of reliability.
'''

'''The Python Tutorial - This section of the official documentation surveys Python's syntax and standard library. It uses examples, and is written using less technical language than the main documentation. Make sure you're reading the Python 3 version of the docs!
The Python Language and Library References - The Language Reference and Library Reference are more technical than the tutorial, but they are the definitive sources of truth. As you become increasingly acquainted with Python you should use these resources more and more.
Third-Party Library Documentation - Third-party libraries publish their documentation on their own websites, and often times at https://readthedocs.org/. You can judge the quality of a third-party library by the quality of its documentation. If the developers haven't found time to write good docs, they probably haven't found the time to polish their library either.
The websites and blogs of prominent experts - The previous resources are primary sources, meaning that they are documentation from the same people who wrote the code being documented. Primary sources are the most reliable. Secondary sources are also extremely valuable. The difficulty with secondary sources is determining the credibility of the source. The websites of authors like Doug Hellmann and developers like Eli Bendersky are excellent. The blog of an unknown author might be excellent, or it might be rubbish.
StackOverflow - This question and answer site has a good amount of traffic, so it's likely that someone has asked (and someone has answered) a related question before! However, answers are provided by volunteers and vary in quality. Always understand solutions before putting them into your program. One line answers without any explanation are dubious. This is a good place to find out more about your question or discover alternative search terms.
Bug Trackers - Sometimes you'll encounter a problem so rare, or so new, that no one has addressed it on StackOverflow. You might find a reference to your error in a bug report on GitHub for instance. These bug reports can be helpful, but you'll probably have to do some original engineering work to solve the problem.
Random Web Forums - Sometimes your search yields references to forums that haven't been active since 2004, or some similarly ancient time. If these are the only resources that address your problem, you should rethink how you're approaching your solution.
'''

# Practice Question
'''Practice Question
For the following practice question you will need to write code in Python in the workspace below. This will allow you to practice the concepts discussed in the Scripting lesson, such as reading and writing files. You will see some older concepts too, but again, we have them there to review and reinforce your understanding of those concepts.

Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).
'''
'''Sample Output:

>>> Enter your First [space] Last name only: Bill Newman
>>> Unique flower name with the first letter: Bellflower
file: flowers.txt

click here to see flowers.txt
my solution: python match_flower_name.py

lower the key of flowers.txt by using str.lower() method
remove the \n at the end by using .strip() method'''
# Write your code here

# HINT: create a dictionary from flowers.txt
flowers = dict()
with open('flowers.txt') as f:
    for line in f:
        (key, value) = line.strip().split(': ')
        flowers[key.lower()] = value

# HINT: create a function to ask for user's first and last name
name = input('Enter your First [space] Last name only: ')
firstLetter = name[0].lower()

# print the desired output
'''print('Unique flower name with the first letter: {}'.format(flowers[firstLetter]))
output

Enter your First [space] Last name only: Bill Newman
Unique flower name with the first letter: Bellflower
answer:

declare a function called create_flowerdict()
take filename as an parameter of create_flowerdict()
# function that creates a flower_dictionary from filenam'''


def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower()
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# Main function that prompts for user input, parses out the first letter
# includes function call for create_flowerdict to create dictionary


def main():
    flower_d = create_flowerdict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(
        flower_d[first_letter]))


main()
