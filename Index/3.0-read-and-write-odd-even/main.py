import sys
import while_loop
import range_loop
import enumerate_loop
import for_loop


def odd_even_loop():
    print("\nWelcome this program for determine even and odd numbers")
    print("Enter 1 for For-Loop\nEnter 2 for While-loop\nEnter 3 for Range-Loop\nEnter 4 for Enumerate loop\nEnter 5 to Exit")
    while True:
        try:
            selection = int(
                input("Enter solution approach using the following options adove: "))

            if selection == 1:
                for_loop.check_even_and_odd_numbers_using_for_loop()
                break
            elif selection == 2:
                while_loop.check_even_number_using_while()
                break
            elif selection == 3:
                range_loop.check_even_and_odd_numbers_using_range_loop()
                break
            elif selection == 4:
                enumerate_loop.checking_even_and_odd_using_enumerate_loop()
                break
            elif selection == 5:
                sys.exit()
                break
            else:
                print("invalid choice. Enter 1-5 using the following options adove:")
                odd_even_loop()
        except ValueError:
            print("invalid choice. Enter 1-5 using the following options adove:")
    exit

    anykey = input("Enter anykey to return to main menu: ")

    odd_even_loop()


odd_even_loop()
