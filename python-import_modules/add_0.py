#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

if __name__ == "__main__":
    # Code here will only execute when this script is run directly, not when imported as a module
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))

    