#!/usr/bin/python3
def element_at(my_list, idx):
    for ele in range(0, len(my_list)):
        if idx < 0 and idx > my_list:
            return None
        else:
            return my_list[idx]
