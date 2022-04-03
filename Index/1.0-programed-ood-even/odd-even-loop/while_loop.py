def check_even_number_using_while(numbers):
    even_number_list = []
    odd_number_list = []
    counter = 1

    print("While loop implementation:")
    while(counter <= numbers):
        if (counter % 2 != 0):
            even_number_list.append(counter)

        else:
            odd_number_list.append(counter)

        counter = counter + 1

    print("Odd numbers: {0}".format(odd_number_list))
    print("Even numbers: {0}".format(even_number_list))
