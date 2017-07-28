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


def query_bool(msg):
    # Asks the user for a boolean response to msg
    from distutils.util import strtobool
    response = ""
    while True:
        try:
            response = strtobool(input(msg + "[y/n]").lower())
        except ValueError:
            continue
        break
    return response


def print_matrix(matrix):
    for row in matrix:
        print("[" + " ".join(map(str, row)) + "]")
