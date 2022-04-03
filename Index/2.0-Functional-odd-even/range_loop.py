def check_even_and_odd_numbers_using_range_loop():
    print("Range loop implementation: ")
    even_number_list = []
    odd_number_list = []
    number = int(input("\nEnter Ending Point: "))

    for num in range(1, number + 2, 1):
        if num % 2 == 0:
            even_number_list.append(num)
            print("Odd numbers: {0}".format(odd_number_list))
        else:
            odd_number_list.append(num)
            print("Even numbers: {0}".format(even_number_list))
