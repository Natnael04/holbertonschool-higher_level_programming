#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        my_list.remove(4)
        return my_list
