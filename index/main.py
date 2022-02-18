import for_loop
import while_loop
import range_loop
import enumerate_loop


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # print("Welcome this program for determine even and odd numbers\n")
    # print("Enter a numbers as you can?\n")
    # print("Select solution approach using the following options below:")
    # print("\n1. While loop\n2. For loop\n3. Range loop\n4. Enumerate loop")

    while_loop.check_even_number_using_while(numbers)
    for_loop.check_even_and_odd_numbers_using_for_loop(numbers)
    range_loop.check_even_and_odd_numbers_using_range_loop()
    enumerate_loop.checking_even_and_odd_using_enumerate_loop(numbers)


main()
