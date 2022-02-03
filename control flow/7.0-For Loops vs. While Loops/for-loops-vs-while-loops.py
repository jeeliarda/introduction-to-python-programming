'''For Loops Vs. While Loops
for loops are ideal when the number of iterations is known or finite.'''

# when we
# have an iterable collection (list, string, set, tuple, dictionary)
#for name in names:

# when we want to
# iterate through a loop for a definite number of times, using range()
'''for i in range(5):
while loops are ideal when the iterations need to continue until a condition is met.'''

# when we want to
# use comparison operators
#while count <= 100:

# when you want to
# loop based on receiving specific user input.
'''while user_input == 'y':
we need to make sure the while loop has:

a condition expression that will be assessed and when met, will allow you to exit the loop
make sure the loop is advancing
the value of the condition variables is changing with each iteration of the loop.
L4-26. Check for Understanding: For and While Loops
Check for Understanding
Q1: There are certain requirements you want to consider adding into a while loop. Which of these requirements must be met? (Select all that apply)

answer	option	reason
(O)	The condition for exiting the while loop should be included	
(O)	Check if the iteration condition is met	
(O)	Body of the loop should change the value of condition variables	
Q2: Question: What type of loop should we use?

You need to write a loop that takes the numbers in a given list named num_list:

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.
'''
#method 1: for loop

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_list = []
result_list = []

for num in num_list:
    if num % 2 == 1:
        odd_list.append(num)

result_list = odd_list[:5]

print(result_list)

#method 2: while loop

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_count = 0
index = 0
result_list = []

while ((odd_count < 5) and (index < len(num_list))):
    if num_list[index] % 2 == 1:
        result_list.append(num_list[index])
        odd_count += 1

    index += 1

print(result_list) # [85, 719, 85, 17, 87]