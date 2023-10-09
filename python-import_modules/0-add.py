#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    # Code here will only execute when this script is run directly, not when imported as a module
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
