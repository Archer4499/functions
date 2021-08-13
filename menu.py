#!/usr/bin/env python3
__author__ = 'Derek King'


def validate_input(str_input, int_min=float("-inf"), int_max=float("inf")):
    # Converts a string to an int within a given range or prints an error message
    class RangeError(Exception):
        pass

    try:
        int_input = int(str_input)
        if int_min <= int_input <= int_max:
            return int_input
        else:
            raise RangeError
    except ValueError:
        print("\n   Please enter a valid integer.")
        return False
    except RangeError:
        if int_max == float('inf'):
            print("\n   Please enter an integer greater than", int_min - 1)
        elif int_min == float('-inf'):
            print("\n   Please enter an integer less than", int_max + 1)
        else:
            print("\n   Please enter an integer between", int_min, "and", int_max)
        return False


def menu(title, *arg):
    # A simple text menu with a variable number of options
    n = len(arg)
    selection = False
    while not selection:
        print("\n" + title + ":")
        for i in range(n):
            print(str(i+1) + ". " + arg[i])
        print(str(n+1) + ". Quit")

        selection = validate_input(input("\nEnter selection: "), 1, n+1)

    if selection == n+1:  # quit
        return False
    else:
        return selection


if __name__ == "__main__":
    result = menu("Menu", "Option 1", "Option 2", "Option 3")
    while result:
        if result == 1:
            print("Option 1")
        elif result == 2:
            print("Option 2")
        elif result == 3:
            print("Option 3")
        result = menu("Option 1", "Option 2", "Option 3")
