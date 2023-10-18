#!/usr/bin/python3
def no_c(my_string):
    remove_cha = "cC"
    new_string = ""
    for char in my_string:
        if char not in remove_cha:
            new_string += char
    return new_string
