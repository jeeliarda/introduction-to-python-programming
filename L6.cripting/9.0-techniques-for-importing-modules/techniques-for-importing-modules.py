'''Techniques for Importing Modules
Techniques for Importing Modules
There are other variants of import statements that are useful in different situations.
To import an individual function or class from a module:
from module_name import object_name
To import multiple individual objects from a module:
from module_name import first_object, second_object
To rename a module:
import module_name as new_name
To import an object from a module and rename it:
from module_name import object_name as new_name
To import every object individually from a module (DO NOT DO THIS):
from module_name import *
If you really want to use all of the objects from a module, use the standard import module_name statement instead and access each of the objects with the dot notation.
import module_name
Modules, Packages, and Names
In order to manage code better, module is split down into sub-modules

A package is simply a module that contains sub-modules

We can only import sub-modules, not functions

import package_name.submodule_name'''

# import os.path

'''when the name of module and class are identical, the name will represent the class

>>> from datetime import datetime
>>> print(datetime)
<class 'datetime.datetime'>'''

# Quiz: Techniques for Importing Modules
'''Importing and accessing from modules
In this quiz, you'll be using different methods to import and use the random.randint() function from the random module. Your task is to match the import statement with the way you would then call the function itself.
'''
# Match the import statement with the way that random.randint() is called

'''IMPORT STATEMENT	CALLING THE FUNCTION
import random	random.randint(0, 10)
from random import randint	randint(0, 10)
import random as rd	rd.randint(0, 10)
from random import randint as rint	rint(0, 10)
from random import *	Don't use this import statement!'''
