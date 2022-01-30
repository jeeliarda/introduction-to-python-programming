'''String: Call by Value
due to string is immutable, so it's call by value'''
name = "Jim"
student = name
name = "Tim"

print(name)     # Tim
print(student)  # Jim

#----------------List Methods
'''len(): how many elements in the list'''

'''max(): greatest elements in the list'''

'''the maximum elements in the list of number is the largest number
the maximum elements in the list of strings is the last element when we sort alphabetically'''

python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']
print(max(python_varieties)) # Reticulated Python

'''undefined for lists that contain elements form different incomparable types'''

max([42, 'African Swallow']) # TypeError: '>' not supported between instances of 'str' and 'int'

'''min(): return the smallest elements in a list'''
'''sorted(): return a copy of a list in order from smallest to largest leaving the original list unchanged'''

sizes = [15, 6, 89, 34, 65, 35]
print(sorted(sizes)) # [6, 15, 34, 35, 65, 89]
print(sorted(sizes, reverse=True)) # [89, 65, 35, 34, 15, 6]

'''join(): takes a list as an argument and returns a string consisting of the list elements joined by separator string'''

nauticla_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nauticla_directions)

'''
fore
aft
starboard
port
'''
'''we can change the separator to -(hyphen)'''

names = ["Garcia", "O'Kelly", "Davis"]
print("-".join(names)) # Garcia-O'Kelly-Davis

'''Although forgetting to add period will not trigger an error, but will give an unexpected results'''
'''this happens bacause of Python's default string literal appending'''

names = ["Garcia", "O'Kelly", "Davis"]
print("-". join(names)) # GarciaO'KellyDavis

'''join() will trigger an error, when we join anything other than string'''

stuff = ["thing", 42, "nope"]
print(" and " .join(stuff)) # TypeError: sequence item 1: expected str instance, int found

'''append(): add the element to the end of the lists'''

python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']

python_varieties.append('Blood Python')

print(python_varieties) # ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python', 'Blood Python']