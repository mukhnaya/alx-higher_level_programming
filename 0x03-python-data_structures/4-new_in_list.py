#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    pau = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > pau:
        return my_list
    else:
        new_lis = my_list.copy()
        new_lis[idx] = element
        return new_lis
