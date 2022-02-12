def E_numbers(numbers, item, num):

    for num, item in enumerate(numbers):
        if num % 2 == 0:
            print("Even numbers: {0}".format(num))
        else:
            print("Odd numbers: {0}".format(num))
