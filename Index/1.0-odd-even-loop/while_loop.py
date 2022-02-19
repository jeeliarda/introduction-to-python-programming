def check_even_number_using_while(numbers):
    even_number_list = []
    odd_number_list = []
    counter = 0

    print("While loop implementation:")
    while(counter < 10):
        num = numbers[counter]
        if num % 2 == 0:
            even_number_list.append(num)
        else:
            odd_number_list.append(num)
        counter = counter + 1

    print("Even numbers: {0}".format(even_number_list))
    print("Odd numbers: {0}".format(odd_number_list))
    print("\n")