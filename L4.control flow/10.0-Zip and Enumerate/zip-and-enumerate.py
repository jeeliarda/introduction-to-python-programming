'''zip and enumerate are useful built-in functions that can come in handy when dealing with loops.
Zip
zip returns an iterator that combines multiple iterables into one sequence of tuples.

Each tuple contains the elements in that position from all the iterables.'''

print(zip(['a', 'b', 'c'], [1, 2, 3])) # <zip object at 0x10b8a9dc8>

print(*zip(['a', 'b', 'c'], [1, 2, 3])) # ('a', 1) ('b', 2) ('c', 3)

print(list(zip(['a', 'b', 'c'], [1, 2, 3]))) # [('a', 1), ('b', 2), ('c', 3)]
#Like we did for range() we need to convert it to a list or iterate through it with a loop to see the elements.
#we could unpack each tuple in a for loop

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

'''
output:
a: 1
b: 2
c: 3
'''
#In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)

print(letters)  # ('a', 'b', 'c')
print(nums)     # (1, 2, 3)
'''Enumerate
enumerate is a built in function that returns an iterator of tuples containing indices and values of a list.
We'll often use this when you want the index along with each element of an iterable in a loop.
without enumerate:'''

letters = ['a', 'b', 'c', 'd', 'e']

'''for i, letter in zip(range(len(letters)), letters):
    print(i, letter)
with enumerate:

#letters = ['a', 'b', 'c', 'd', 'e']
#for i, letter in enumerate(letters):
print(i, letter)'''

'''output:
0 a
1 b
2 c
3 d
4 e'''

'''Quiz: Zip and Enumerate
Quiz: Zip Coordinates
Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.'''

'''In the example below, label, x, y, z equals to *point
the tuple was unpacked using * in the format method. This can help making code cleaner!'''

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here

for point in zip(labels, x_coord, y_coord, z_coord):
    # label, x, y, z = point
    # points.append("{}: {}, {}, {}".format(label, x, y, z))
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)

'''
output:
F: 23, 677, 4
J: 53, 233, 16
A: 2, 405, -6
Q: -12, 433, -42
Y: 95, 905, 3
B: 103, 376, -6
W: 14, 432, 23
X: -5, 445, -1
'''
'''Quiz: Zip Lists to a Dictionary
Use zip to create a dictionary cast that uses names as keys and heights as values.'''

#my solution:

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict()

for cast_name, cast_height in zip(cast_names, cast_heights):
    cast[cast_name] = cast_height

print(cast)

'''
output:
{'Barney': 72, 'Robin': 68, 'Ted': 72, 'Lily': 66, 'Marshall': 76}
'''
#answer:

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

'''
output:
{'Barney': 72, 'Robin': 68, 'Ted': 72, 'Lily': 66, 'Marshall': 76}
'''
#The order of elements in this output may vary since dictionaries are unordered.

#Quiz: Transpose with Zip
#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.

#my solution:

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple()

# for a, b, c, d in zip(data[0], data[1], data[2], data[3]):
#     data_transpose += (a, b, c, d,)

for x in zip(*data):
    data_transpose += (x, )

print(data_transpose)

'''
output:
((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))
'''
#answer:

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

'''
output:
((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))
'''
'''Quiz: Enumerate
Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height. For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".'''

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for index, name in enumerate(cast):
    cast[index] = "{} {}".format(name, heights[index])

print(cast)

'''
output:
['Barney Stinson 72', 'Robin Scherbatsky 68', 'Ted Mosby 72', 'Lily Aldrin 66', 'Marshall Eriksen 76']
'''
#if we don't want to use .format() method, we can use += operator alternatively, but remember to convert the type to str

#wrong:

# hide cast and heights variable
for index, name in enumerate(cast):
    cast[index] += name + " " + heights[index] # TypeError: Can't convert 'int' object to str implicitly

print(cast)
#right:

# hide cast and heights variable
for index, name in enumerate(cast):
    cast[index] += name + " " + str(heights[index])

'''print(cast)
Diff between point, *point
In the example below, we have the same variables x_coord, y_coord, labels and points'''

x_coord = [23, 53]
y_coord = [677, 233]
labels = ["F", "J"]
points = []
#1. point
#the type of point IS <class 'tuple'>

point = (labels[0], x_coord[0], y_coord[0])

for point in zip(labels, x_coord, y_coord):
    print(point)

'''
output:
('F', 23, 677)
('J', 53, 233)
'''
#2. *point
'''the asterisk(*) here is used for unpacking the tuple point

the type of *point is NOT <class 'tuple'>

*point = labels[0], x_coord[0], y_coord[0]'''

for point in zip(labels, x_coord, y_coord):
    print(*point)

'''
output:
F 23 677
J 53 233
'''
#3. *point with foramt()
for point in zip(labels, x_coord, y_coord):
    print("{}: {} x {}".format(*point))

'''
output:
F: 23 x 677
J: 53 x 233
'''