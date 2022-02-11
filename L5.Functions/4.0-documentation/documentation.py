'''Documentation is used to make code easier to understand and use

docstrings, or documentation strings: a type of comment used to explain the purpose of a function, and how it should be used

docstring is optional, however, it's a good coding practice
single line docstrings are perfectly acceptable

docstrings are surrounded by triple quotes(""")'''
#the first line of the docstrings is a brief explanation of the function's purpose
def population_density(population, land_area):
#Calculate the population density of an area.
#return population / land_area
#If longer description would be appropriate for the function, we can add more information like the type and purpose of function's arguments, input and output

#def population_density(population, land_area):
#Calculate the population density of an area.
#INPUT:
#population: int. The population of the area
#land_area: int or float. This function is unit-agnostic, if you pass in values in terms of square km or square miles the function will return a density in those units.

#OUTPUT:
#population_density: population/land_area. The population density of a particular area.

#return population / land_area

#we can click here to read more details about docstrings

#Quiz: Documentation
#Quiz: Write a Docstring
#Write a docstring for the readable_timedelta function you defined earlier! Remember the way you write your docstrings is pretty flexible! Look through Python's docstring conventions here and check out this Stack Overflow page for some inspiration!'''

#my solution:

#def readable_timedelta(days):
    # insert your docstring here
    """convert days into weeks and days"""

    #weeks = days // 7
    #remainder = days % 7
    #return "{} week(s) and {} day(s)".format(weeks, remainder)

#types of answer:

"""Return a string of the number of weeks and days included in days."""
"""Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert
    """
"""
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """