import numbers
from operator import itemgetter


def checking_even_and_odd_using_enumerate_loop():
    print("Enumerate loop implementation:")
    even_number_list = []
    odd_number_list = []
    list_numbers = []

    
    i = 1
    while i!=0:
        number = int(input("\nEnter a Number: "))
        list_numbers.append(number)

        print("list_numbers:")
        print(list_numbers)
        str_option = str(input("\nYou would like continue, please enter 'y' if yes. If yo want to exit, kindly type 'n' "))
        if str_option=='y':
            i = i + 1
        else:
            i = 0


    for num, item in enumerate(list_numbers):
        if num % 2 == 0:
            even_number_list.append(num)

        else:
            odd_number_list.append(num)
    print("\nOdd numbers: {0}".format(odd_number_list))
    print("\nEven numbers: {0}".format(even_number_list))
    print("\n")
