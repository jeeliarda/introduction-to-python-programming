def odd_even_loop():
    print("Welcome this program for determine even and odd numbers\n")
    print("Enter 1 for For-Loop\nEnter 2 for While-loop\nEnter 3 for Range-Loop\nEnter 4 for Enumerate loop\nEnter 5 to Exit")
    while True:
        try:
            selection = int(
                input("Enter solution approach using the following options adove:"))
            if selection == 1:
                for_loop()
                break
            elif selection == 2:
                while_loop()
                break
            elif selection == 3:
                range_loop()
                break
            elif selection == 4:
                enumerate_loop()
                break
            elif selection == 5:
                break
            else:
                print("invalid choice. Enter 1-5")
                odd_even_loop()
        except ValueError:
            print("invalid choice. Enter 1-5")
    exit

def for_loop():
    print("for")
    anykey = input("Enter anykey to return to main menu: ")
    odd_even_loop()

def while_loop():
    print("while")
    anykey = input("Enter anykey to return to main menu: ")
    odd_even_loop()

def range_loop():
    print("range")
    anykey = input("Enter anykey to return to main menu: ")
    odd_even_loop()

def enumerate_loop():
    print("enumerate")
    anykey = input("Enter anykey to return to main menu: ")
    odd_even_loop()


odd_even_loop()
