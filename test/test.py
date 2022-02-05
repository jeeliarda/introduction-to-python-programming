'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for odd in numbers:
    if odd == 10:
        print(str(odd))
        break;
    elif odd %  == 0:
        print(odd)'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8,9,10]

# for num in numbers:
#    if num % 2==0:
#        print("Even numbers: {0}".format(num))
#    else:
#         print("Odd numbers: {0}".format(num))


'''numbers = [1, 2, 3, 4, 5, 6, 7, 8,9,10]

counter =0
while(counter<10):
    num = numbers[counter]
if num % 2==0:
    print("Even numbers: {0}".format(num))
else:
    print("Odd numbers: {0}".format(num))
counter = counter + 1'''



'''for num in range(10):
    if num % 2==0:
        print("Even numbers: {0}".format(num))
    else:
        print("Odd numbers: {0}".format(num))'''


numbers = [1, 2, 3, 4, 5, 6, 7, 8,9,10]

for num in enumerate(numbers):
    if num % 2==0:
        print("Even numbers: {0}".format(num))
else:
    print("Odd numbers: {0}".format(num))