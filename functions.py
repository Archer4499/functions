#!/usr/bin/env python3
__author__ = 'Derek King'


def validate_input(str_input, int_min=float("-inf"), int_max=float("inf")):
    # Converts a string to an int within a given range
    #  or prints an error message and returns None
    try:
        int_input = int(str_input)
    except ValueError:
        # Int parsing fails
        print("\n   Please enter a valid integer")
        return None

    if int_min <= int_input <= int_max:
        # Valid int in range
        return int_input
    else:
        if int_max == float('inf'):
            print("\n   Please enter an integer greater than", int_min - 1)
        elif int_min == float('-inf'):
            print("\n   Please enter an integer less than", int_max + 1)
        else:
            print("\n   Please enter an integer between", int_min, "and", int_max)
        return None


def query_bool(msg):
    # Asks the user for a boolean response to msg
    #  msg: a string question to be printed with a [y/n] appended directly without any space
    from distutils.util import strtobool
    response = ""
    while True:
        try:
            response = strtobool(input(msg + "[y/n]").lower())
        except ValueError:
            continue
        break
    return response

def query_bool_with_default(msg, default=None):
    # Asks the user for a boolean response to msg
    #  msg: a string question to be printed with a [y/n] appended directly without any space
    #  default: takes a boolean to set the default selection if no text is input in response to the question
    from distutils.util import strtobool
    response = ""
    while True:
        try:
            if default is None:
                # No default
                answer = input(msg + "[y/n]").lower()
            elif default is False:
                # Default is No
                answer = input(msg + "[y/N]").lower()
                if answer == "":
                    return False
            else:
                # Default is Yes
                answer = input(msg + "[Y/n]").lower()
                if answer == "":
                    return True

            response = strtobool(answer)
        except ValueError:
            continue
        break
    return response


def print_matrix(matrix):
    for row in matrix:
        print("[" + " ".join(map(str, row)) + "]")


def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def write_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as f:
        for line in data:
            f.write(line + "\n")


def list_of_str_to_str(inp_list):
    return ",".join(inp_list)

def list_of_other_to_str(inp_list):
    return ",".join(map(str, inp_list))
