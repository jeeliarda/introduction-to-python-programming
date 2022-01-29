# we can assign multiple variables at once

# x = 2
# y = 3
# z = 5
x, y, z = 2, 3, 5
# add meaningful variable name, to improve readability

population = 1000
area = 10
density = population / area
print(density) # 100

#only use ordinary letters, numbers or underscores
#can't have spaces
#need to start with a letter or underscore


#can't use reserved words or build-in identifiers

#snake case: use all lowercase letters and underscores to separate words

#---------Execise-----------

#Scientific Notation
#all three numbers below are equal, the type of scientific notation is float
4.445e8         # 444500000.0
4.445 * 10 ** 8 # 444500000.0
444500000.0     # 444500000.0
#Q3: Here is a list of U.S. states in order of the date they entered the Union. Say you wanted to create a variable for Delaware and assign it a value to signify that it joined the Union first. Which of the following are valid variable names and assignments in Python?

#answer	option	reason
#del = 1	del is a reserved word
#(O)	delaware = 1	
#1 de = first	can't have space, should start with a letter or underscore
#(O)	de = 1	

#--------QUIZ--------------

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff

rainfall -= rainfall*0.1

# add the rainfall variable to the reservoir_volume variable
reservoir_volume  += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
reservoir_volume += reservoir_volume*0.05
# into the reservoir in the days following the storm
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -= reservoir_volume*0.05
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)

#Quiz: Changing Variable Values
#How does changing the value of a variable affect another variable that was defined in terms of it? Let's look at an example.

#We're intentionally not providing a place to execute the code here, because we want to help you practice the important skill of walking through lines of code by hand.

#Each line of code executes in order, one at a time, with control going from one line to the next.

#>>> carrots = 24
#>>> rabbits = 8
#>>> crs_per_rab = carrots/rabbits

#Now we add a new 4th line to this code, that assigns a new value to the rabbits variable:

#>>> rabbits = 12


#QUESTION 3 OF 3
#Here is a list of U.S. states in order of the date they entered the Union. Say you wanted to create a variable for Delaware and assign it a value to signify that it joined the Union first. Which of the following are valid variable names and assignments in Python?


delaware = 1


de = 1

