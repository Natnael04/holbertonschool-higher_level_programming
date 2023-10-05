#!/usr/bin/python3
def add(a, b):
    return a + b
if __name__ == "__main__":
    # Code here will only execute when this script is run directly, not when imported as a module
    a = 1
    b = 2
    result = add(1, 2)
    print("{} + {} = {}".format(a, b, result))
