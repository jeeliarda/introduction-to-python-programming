# Practice Debugging
# The following are some common exceptions. Again, "exceptions" are errors detected during execution.

'''EXAMPLE EXCEPTION	HOW WOULD YOU TRY TO HANDLE THE EXCEPTION?
UnboundLocalError	You are trying to access a local variable before it is defined. Make sure local scope of variable in function is defined or value assigned to it.
L6-22. Importing Local Scripts
Importing Local Scripts
importing python script from other files is useful when working on a bigger project

format: import followed by the name of the file, without the .py extension'''

'''import useful_functions
Conventionally, we write import statement at the top of the file

Import statement will create a module object

Modules are just Python files that contain definitions and statements.
To access objects from an imported module, you need to use dot notation
import useful_functions
useful_functions.add_five([1, 2, 3, 4])
we can add an alias by using as statment'''

'''import useful_functions as uf
Using a main block
Whenever we run a script like this, Python actually sets a special built-in variable called __name__ for any module
When we run a script, Python recognizes this module as the main program, and sets the __name__ variable for this module to the string "__main__".
For any modules that are imported in this script, this built-in __name__ variable is just set to the name of that module.
Therefore, the condition if __name__ == "__main__" is just checking whether this module is the main program.
Example
file: demo.py
'''
#import useful_functions as uf

scores = [88, 92, 79, 93, 85]

'''mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)'''

'''print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)     # __main__
print(uf.__name__)  # useful_functions'''

# output

'''Scores: [88, 92, 79, 93, 85]
Original Mean: 87.4  New Mean: 92.4
__main__'''

'''useful_functions
file: useful_functions.py
'''


def mean(num_list):
    return sum(num_list) / len(num_list)


def add_five(num_list):
    return [n + 5 for n in num_list]  # list comprehension


def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")


if __name__ == '__main__':  # only execute when we run 'useful_functions.py'
    main()
# output

'''Testing mean function
Testing add_five function
All tests passed!'''
