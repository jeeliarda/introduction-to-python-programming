def checking_even_and_odd_using_enumerate_loop():
    print("Enumerate loop implementation:")
    even_number_list = []
    odd_number_list = []
    list_numbers = []

    i = 1
    while i != 0:

        str_option = str(input(
            "\nYou would like continue, please enter 'y' if yes. If yo want to exit, kindly type 'n' "))
        if str_option == 'y':
            number = int(input("\nEnter a Number: "))
            list_numbers.append(str(number))

            print("list_numbers:")
            print(list_numbers)
            i = i + 1
        elif str_option == 'n':
            i = 0

    print(list_numbers)
    for index, item in enumerate(list_numbers):
        print("item: ")
        print(item)
        print("index: ")
        print(index)
        if int(item) % 2 == 0:
            print("item of even: ")
            print(item)
            even_number_list.append(str(item))
        else:
            print("item of odd: ")
            print(item)
            odd_number_list.append(str(item))


checking_even_and_odd_using_enumerate_loop()
