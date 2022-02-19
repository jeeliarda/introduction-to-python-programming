import numbers
from operator import itemgetter


def checking_even_and_odd_using_enumerate_loop():
    print("Enumerate loop implementation:")
    even_number_list = []
    odd_number_list = []
    number = int(input("\nEnter a Number: "))

    for num, item in enumerate([number]):
        if num % 2 == 0:
            even_number_list.append(num)

        else:
            odd_number_list.append(num)
    print("\nOdd numbers: {0}".format(odd_number_list))
    print("\nEven numbers: {0}".format(even_number_list))
    print("\n")
