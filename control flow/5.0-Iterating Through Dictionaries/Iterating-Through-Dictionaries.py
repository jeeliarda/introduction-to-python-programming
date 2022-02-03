'''Iterating Through Dictionaries with For Loops
the dictionary cast contains these keys and values'''
cast = {
        "Jerry Seinfeld": "Jerry Seinfeld",
        "Julia Louis-Dreyfus": "Elaine Benes",
        "Jason Alexander": "George Costanza",
        "Michael Richards": "Cosmo Kramer"
    }

#Iterating through it in the usual way with a for loop would give you just the keys
for key in cast:
    print(key)

'''
output:
Jerry Seinfeld
Julia Louis-Dreyfus
Jason Alexander
Michael Richards
'''
#If we wish to iterate through both keys and values, we can use the built-in method items like this:
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

'''
output:
Actor: Jerry Seinfeld    Role: Jerry Seinfeld
Actor: Julia Louis-Dreyfus    Role: Elaine Benes
Actor: Jason Alexander    Role: George Costanza
Actor: Michael Richards    Role: Cosmo Kramer
'''
#items is an awesome method that returns tuples of key, value pairs
print(cast.items())

'''
output:
dict_items([('Jerry Seinfeld', 'Jerry Seinfeld'), ('Julia Louis-Dreyfus', 'Elaine Benes'), ('Jason Alexander', 'George Costanza'), ('Michael Richards', 'Cosmo Kramer')])
'''