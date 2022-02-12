def f_numbers(num, numbers):

    for num in numbers:
        if num % 2 == 0:
            print("Even numbers: {0}".format(num))
        else:
            print("Odd numbers: {0}".format(num))
