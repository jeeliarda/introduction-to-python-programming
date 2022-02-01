
#boolean
bool_light_on=False

if bool_light_on==True:
    print("On")
else:
    print("Off")

#check if number equal to zero
"""number = 0

if number==0:
    print("number")
else:
    print("not number")"""


#Checking if the number is greater than by 6
''''number = 7
if number>6:
    print("True")
else:
    print("False")'''

#Checking if the number is equal to four by using elif
'''number = 4
if number<4:
    print("True")
elif number==4:
    print("Yes they are equal")
else:
    print("false")'''

# and conditon
# number>6 = True 
# (number < 8) = True
'''number = 7
condition1 = number>6 # True
condition2 = number < 6 #True
if condition1 and condition2:
    print("True")
else:
    print("False")'''

# using or conditon
'''number = 7
condition1 = number>6 # True
condition2 = number < 6 #True
if condition1 or condition2:
    print("True")
else:
    print("False")'''


#using not conditon
light=True

myvariable1 = (light==True)
myvariable2 = not myvariable1

if not (light==True):
    print("Light is on")
else:
    print("no light")


'''= vs ==

=: assign operator
==: comparison operator
Indentation
Unlike other programming language using braces to enclose block of code
In python, we use indentation to enclose block of code.
This indentation conventionally comes in multiples of four spaces.
It's important to be strict about following this convention.
Spaces or Tabs?
The Python Style Guide recommends using 4 spaces to indent, rather than using a tab.
Whichever you use, be aware that "Python 3 disallows mixing the use of tabs and spaces for indentation."'''
