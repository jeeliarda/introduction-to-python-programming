'''While Loops
For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times.
"indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met, which is what happens in a while loop.'''
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand) < 17:
    hand.append(card_deck.pop())
    print(sum(hand))

print(hand)

'''
output:
10
18
[10, 8]
'''
'''The indented body of the loop should modify at least one variable in the test condition.
If the value of the test condition never changes, the result is an infinite loop!
doc
sum(iterable, /, start=0)
sum(iterable, /, start=0)
L4-21. Practice: While Loops
Practice: Factorials with While Loops'''

# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while (current <= number):
    # multiply the product so far by the current number
    product *= current

    # increment current with each iteration until it reaches number
    current += 1



# print the factorial of number
print(product) # 720

'''Practice: Factorials with For Loops'''
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
# for i in range(1, number): # (X) exit at number 6-1
# for i in range(1, number+1): # (△) exit at number 6
for i in range(2, number+1): # (O) there's no need to mutiple by 1
    product *= i


# print the factorial of number
print(product) # 720

'''L4-23. Quiz: While Loops
Quiz: Nearest Square
Write a while loop that finds the largest square number less than an integer limit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

For example, if limit is 40, your code should set the nearest_square to 36.

my answer:'''

limit = 40

# write your while loop here

root = 1
nearest_square = 0
square = root**2
while (square < limit):
    nearest_square = square
    root += 1
    square = root**2

print(nearest_square)

#solution:

limit = 40

num = 0 # start from 0
while (num+1)**2 < limit: # +1 is the key point
    num += 1
nearest_square = num**2

print(nearest_square)