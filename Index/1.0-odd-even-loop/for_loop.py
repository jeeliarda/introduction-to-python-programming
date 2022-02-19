def check_even_and_odd_numbers_using_for_loop(numbers):
    even_number_list = []
    odd_number_list = []

    print("For loop implementation:")
    for num in numbers:
        if num % 2 == 0:
            even_number_list.append(num)
        else:
            odd_number_list.append(num)

    print("Even numbers: {0}".format(even_number_list))
    print("Odd numbers: {0}".format(odd_number_list))
    print("\n")
