def check_even_and_odd_numbers_using_for_loop():
    even_number_list = []
    odd_number_list = []
    numbers = []
    data = int(input("\nEnter a number: "))
    numbers.append(data)

    print("\nFor loop implementation:")
    for num in numbers:
        if num % 2 == 0:
            even_number_list.append(num)
            print("\nEven numbers: {0}".format(even_number_list))
        else:
            odd_number_list.append(num)
            print("\nOdd numbers: {0}".format(odd_number_list))
    print("\n")
