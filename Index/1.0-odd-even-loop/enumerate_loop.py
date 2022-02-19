def checking_even_and_odd_using_enumerate_loop(numbers):
    print("Enumerate loop implementation:")
    even_number_list = []
    odd_number_list = []

    for num, item in enumerate(numbers):
        if num % 2 == 0:
            even_number_list.append(num)
        else:
            odd_number_list.append(num)


    print("Even numbers: {0}".format(even_number_list))
    print("Odd numbers: {0}".format(odd_number_list))
    print("\n")