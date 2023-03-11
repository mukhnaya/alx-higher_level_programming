#!/usr/bin/python3
def element_at(my_list, idx):
    pau = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > pau:
        return None
    return my_list[idx]
