def check_even_number_using_while():

    even_number_list = []
    odd_number_list = []
    start = int(input("\nEnter Starting Point: "))
    end = int(input("Enter The Ending Point: "))
    counter = start

    print("\nWhile loop implementation:")
    while(counter <= end):
        if (counter % 2 != 0):
            even_number_list.append(counter)

        else:
            odd_number_list.append(counter)

        counter = counter + 1

    print("\nOdd numbers: {0}".format(odd_number_list))
    print("\nEven numbers: {0}".format(even_number_list))
    print("\n")
