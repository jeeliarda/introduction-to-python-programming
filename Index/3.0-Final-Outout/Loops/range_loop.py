def check_even_and_odd_numbers_using_range_loop():
    print("Range loop implementation: ")
    even_number_list = []
    odd_number_list = []
    number = int(input("\nEnter Ending Point: "))

    for num in range(number):
        if num % 2 == 0:
            even_number_list.append(num)

        else:
            odd_number_list.append(num)
    # print("\nOdd numbers: {0}".format(odd_number_list))
    # print("\nEven numbers: {0}".format(even_number_list))
    # print("\n")
   #1. create a file
   #2. write the output in the file
   #3. Read
    write_file("data")


def write_file(data):
    pass

def read_file():
    pass