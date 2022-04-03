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

    odd_number_list = str(odd_number_list)
    oddfile = open(
        'C:\\code\\introduction-to-python-programming\\Index\\3.0-read-and-write-odd-even\\json\\oddfile.json', 'w')
    oddfile.write(odd_number_list)
    oddfile.close()

    oddfile = open(
        'C:\\code\\introduction-to-python-programming\\Index\\3.0-read-and-write-odd-even\\json\\oddfile.json', 'r')
    lines = oddfile.readlines()
    oddfile.close()
    print("\nOdd numbers: {0}".format(lines))
    print("\n")
