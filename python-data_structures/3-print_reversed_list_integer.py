#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        my_list = []
    new_list = my_list[::-1]
    for item in new_list:
        print("{:d}".format(item))
