# numbers = [1, 2, 3, 4, 5, 6, 7, 8,9,10]

# for num in numbers:
#    if num % 2==0:
#        print("Even numbers: {0}".format(num))
#    else:
#         print("Odd numbers: {0}".format(num))



def even_and_odd_numbers(numbers,counter, even_number_list, odd_number_list):
        while(counter<10):
                num = numbers[counter]
                if num % 2==0:
                        even_number_list.append(num)
        else:
                odd_number_list.append(num)
        counter = counter + 1


        print("Even numbers: {0}".format(even_number_list))
        print("Odd numbers: {0}".format(odd_number_list))