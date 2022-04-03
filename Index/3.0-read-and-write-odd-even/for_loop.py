def check_even_and_odd_numbers_using_for_loop():
    even_number_list = []
    odd_number_list = []
    numbers = []
    data = int(input("\nEnter a number: "))
    numbers.append(data)

    for num in numbers:
        if num % 2 == 0:
            even_number_list.append(num)
            #print("\nEven numbers: {0}".format(even_number_list))
            even_number_list = str(even_number_list)
            evenfile = open(
                'C:\\code\\introduction-to-python-programming\\Index\\3.0-read-and-write-odd-even\\json\\evenfile.json', 'w')
            evenfile.write(even_number_list)
            evenfile.close()

            evenfile = open(
                'C:\\code\\introduction-to-python-programming\\Index\\3.0-read-and-write-odd-even\\json\\evenfile.json', 'r')
            lines = evenfile.readlines()
            print("\nEven numbers: {0}".format(lines))
            evenfile.close()
        else:
            odd_number_list.append(num)
            #print("\nOdd numbers: {0}".format(odd_number_list))
            odd_number_list = str(odd_number_list)
            oddfile = open(
                'C:\\code\\introduction-to-python-programming\\Index\\3.0-read-and-write-odd-even\\json\\oddfile.json', 'w')
            oddfile.write(odd_number_list)
            oddfile.close()

            oddfile = open(
                'C:\\code\\introduction-to-python-programming\\Index\\3.0-read-and-write-odd-even\\json\\oddfile.json', 'r')
            lines = oddfile.readlines()
            print("\nOdd numbers: {0}".format(lines))
            oddfile.close()
    print("\n")
