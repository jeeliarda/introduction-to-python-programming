#Coding Quiz: Check for Prime Numbers

'''Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

For instance, 6 has four factors: 1, 2, 3, 6.

1 X 6 = 6
2 X 3 = 6
So we know 6 is not a prime number.

In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.

If the numbers are prime, the code should print "[number] is a prime number."

If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".

Example output:

7 IS a prime number
26 is NOT a prime number, because 2 is a factor of 26
my solution:

the optimal range is from 2 to sqrt(number) or 2 <= x <= sqrt(number)

number**(1/2) means sqrt(number)'''

#int(): cut the number after decimal point(not round off)

print(int(1.6))  #  1
print(int(-1.6)) # -1

#if number is 11, int(number**(1/2)) is 3, thus we have to add 1

## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for number in check_prime:
    for i in range(2, int(number**(1/2)) + 1):
        if (number%i == 0):
            factor = i
            print("{} is NOT a prime number, because {} is a factor of {}".format(number, factor, number))
            break

    else: # we can use for...else clause to reduce the use of flags
        print("{} IS a prime number".format(number))

'''
output:
26 is NOT a prime number, because 2 is a factor of 26
39 is NOT a prime number, because 3 is a factor of 39
51 is NOT a prime number, because 3 is a factor of 51
53 IS a prime number
57 is NOT a prime number, because 3 is a factor of 57
79 IS a prime number
85 is NOT a prime number, because 5 is a factor of 85
'''
'''for... else
purpose: reduce the use of unnecessary fla'''

#before:

nums = [60, 70, 30, 110, 90]
found = False # the flag that can remove
for n in nums:
    if n > 100:
        found = True # the flag that can remove
        print("There is a number bigger than 100")
        break

if not found: # the expression that can remove
    print("Not found!")

#after:

nums = [60, 70, 30, 110, 90]
for n in nums:
    if n > 100:
        print("There is a number bigger than 100")
        break
else:
    print("Not found!")