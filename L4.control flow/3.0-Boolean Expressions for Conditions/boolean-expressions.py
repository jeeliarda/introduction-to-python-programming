'''Complex Boolean Expressions'''
if 18.5 <= weight / height**2 < 25: # height ** 2 compute first
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
'''For really complicated conditions you might need to combine some ands, ors and nots together.
Use parentheses if you need to make the combinations clear.'''

'''1. Don't use True or False as conditions
it's useless to use any condition that you know will always evaluate to True or False'''

# Bad example
if True:
    print("This indented code will always get run.")

# Another bad example
if is_cold or not is_cold:
    print("This indented code will always get run.")

'''2. Be careful writing expressions that use logical operators
Logical operators and, or and not have specific meanings that aren't quite the same as their meanings in plain English.'''

# Bad example
if weather == "snow" or "rain":
    print("Wear boots!")

# Good example
if weather == "snow" or weather == "rain":
    print("Wear boots!")


'''Later we'll discuss what happens when we use non-boolean-type objects in place of booleans.'''

if "rain": # evaluate result is True
    print("Wear boots!") # Wear boots!

'''3. Don't compare a boolean variable with == True or == False
This comparison isn’t necessary, since the boolean variable itself is a boolean expression.'''

# Bad example
if is_cold == True:
    print("The weather is cold!")

# Good example, discard unnecessary words
if is_cold:
    print("The weather is cold!")
'''If you want to check whether a boolean is False, you can use the not operator.'''

# Bad example
if is_hot == False:
    print("The weather is cold!")

# Good example, use "not" operator
if not is_hot:
    print("The weather is cold!")

'''Here are most of the built-in objects that are considered False in Python:

constants defined to be false: None and False
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '"", (), [], {}, set(), range(0)
example:'''

errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")

# Output: You have 3 errors to fix!