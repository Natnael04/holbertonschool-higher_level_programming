#!/usr/bin/python3
import sys


def main():
    # Get the command-line arguments (excluding the script name)
    arguments = sys.argv[1:]

    # Initialize a variable to store the sum
    total_sum = 0

    # Iterate through the arguments and sum up the integer ones
    for arg in arguments:
        if arg.isdigit() or (arg[0] == '-' and arg[1:].isdigit()):
            total_sum += int(arg)

    # Print the result of the addition
    print(f"{total_sum}")


if __name__ == "__main__":
    main()
