#!/usr/bin/python3
def no_c(my_string):
    unwanted = ["c", "C"]
    my_string = '' .join(i for i in my_string if not i in unwanted)
    return my_string
    print("" + str(my_string))
