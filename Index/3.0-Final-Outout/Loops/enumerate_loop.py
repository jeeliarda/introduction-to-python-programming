import numbers
from operator import itemgetter


def checking_even_and_odd_using_enumerate_loop():
    print("Enumerate loop implementation:")
    even_number_list = []
    odd_number_list = []
    list_numbers = []

    
    i = 1
    while i!=0:
       
        str_option = str(input("\nYou would like continue, please enter 'y' if yes. If yo want to exit, kindly type 'n' "))
        if str_option=='y':
            number = int(input("\nEnter a Number: "))
            list_numbers.append(str(number))

            print("list_numbers:")
            print(list_numbers)
            i = i + 1
        elif str_option=='n':
            i = 0

    #1. Write the data into a file
    # list_numbers ["1", "2"]
    #file1.json
    #["1", "2"]
    
    #2. Get the data from file (Read a file from file1.json)
    #["1", "2"]
    #put on the variable or param variable
    # example:
    #from file: list_numbers = ["1", "2"]
    #data = json.loads(list_numbers) or json.dumps(list_numbers)
    print(list_numbers)
    for num, item in enumerate(list_numbers):
        print("item: ")
        print(item)
        print("num: ")
        print(num)
        if int(item) % 2 == 0:
            print("item of even: ")
            print(item)
            even_number_list.append(str(item))
        else:
            print("item of odd: ")
            print(item)
            odd_number_list.append(str(item))


    print("\nOdd numbers: {0}".format(odd_number_list))
    print("\nEven numbers: {0}".format(even_number_list))
    print("\n")


    # for num, item in enumerate(list_numbers):
    #     if int(num) % 2 == 0:
    #         even_number_list.append(num)

    #     else:
    #         odd_number_list.append(num)
    # print("\nOdd numbers: {0}".format(odd_number_list))
    # print("\nEven numbers: {0}".format(even_number_list))
    # print("\n")
