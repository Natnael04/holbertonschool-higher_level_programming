#!/usr/bin/python3
import sys


def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print(f"{num_arguments} arguments.")
    else:
        print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}:")
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
