'''Reading and Writing Files
Reading a File
f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()
open the file using built-in method open(), it returns a file object.
there're optional parameters we can specify in Python. Here we use r for read only. This's the default value for the mode argument.
use the read() method to access the contents from the file object.
when finished with the file, don't forget to use close() to free up memory.
Writing to a File
f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()
open the file in writing(w) mode
if the file doesn't exist, python will create it for us
if we open an existed file, any contents contained previously will be deleted
if we don't want to add files without deleting contents, we should use append(a) mode
use the write() method to write text to a file
close the file when finished
Too Many Open Files
we shouldn't open too many files without close it.

files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)
output

...
5850
5851
5852
Traceback (most recent call last):
File "tempCodeRunnerFile.python", line 3, in <module>
OSError: [Errno 23] Too many open files in system: 'some_file.txt'
With
Python provides a special syntax that auto-closes a file for us once we're finished using it.
'''
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()
    # we don't need to close a file manually

print(f)  # (X) we can only access the file object within 'with' scope
print(file_data)  # (O) we can still access variable outside 'with' scope


# Quiz: Reading and Writing Files
'''Calling the read Method with an Integer
if we don't pass any argument to f.read(), this defaults to reading all the remainder of the file from its current position
if we pass with integer argument, it will read up to that number of characters, output all of them, and keep the 'window' at that position ready to read on.
input: camelot.txt
'''
'''We're the knights of the round table
We dance whenever we're able
script'''

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

# output

'''We
're the 
knights of the round table
We dance whenever we're able
Reading Line by Line
\ns in blocks of text are newline characters.
f.readline()
we can use f.readline() to read a single line from the file'''

with open("camelot.txt") as f:
    print(f.readline())
    print(f.readline())

# output

'''there're unnecessary new lines
We're the knights of the round table

We dance whenever we're able

we can use .strip() to remove the unnecessary new lines'''

with open("camelot.txt") as f:
    print(f.readline().strip())
    print(f.readline().strip())

# output

'''We're the knights of the round table
We dance whenever we're able
for line in file
Conveniently, Python will loop over the lines of a file using the syntax for line in file.'''

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

# output

'''["We're the knights of the round table", "We dance whenever we're able"]
we use .strip() to remove trailing \n before, if we don't add .strip():'''

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line)

print(camelot_lines)

# output

'''every elements except for the last element will have a trailing \n
["We're the knights of the round table\n", "We dance whenever we're able"]
f.readlines()
or we can just use f.readlines()'''

with open("camelot.txt") as f:
    print(f.readlines())

# output

'''every elements except for last element will have a trailing \n
["We're the knights of the round table\n", "We dance whenever we're able"]
we can't just add .strip() after readlines(), because it returns an list'''

with open("camelot.txt") as f:
    print(f.readlines().strip())

# output

'''Traceback (most recent call last):
File "tempCodeRunnerFile.python", line 2, in <module>
    print(f.readlines().strip())
AttributeError: 'list' object has no attribute 'strip'/'''

'''Quiz: Flying Circus Cast List
You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

Write a function called create_cast_list that takes a filename as input and returns a list of actors' names. It will be run on the file flying_circus_cast.txt (this information was collected from imdb.com). Each line of that file consists of an actor's name, a comma, and then some (messy) information about roles they played in the programme. You'll need to extract only the name and add it to a list. You might use the .split() method to process each line.

file: flying_circus_cast.txt

click here to see the file'''

# answer:


def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    # use the for loop syntax to process each line
    # and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            cast_list.append(line.split(",")[0])

    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)


# answer:

# add a new variable name to separate into two lines
def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
'''doc
read([size[, chars[, firstline]]])
read([size[, chars[, firstline]]])
readline([size[, keepends]])
readline([size[, keepends]])
readlines([sizehint[, keepends]])
readlines([sizehint[, keepends]])
str.strip([chars])
str.strip([chars])'''
