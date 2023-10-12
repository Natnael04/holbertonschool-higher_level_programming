#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    if my_list is None:
        my_list = []
    for item in new_list:
        print("{:d}".format(item))
