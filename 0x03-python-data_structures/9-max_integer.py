#!/usr/bin/python3
def max_integer(my_list=[]):
    pau = len(my_list) - 1
    x = pau
    if pau == 0:
        return None
    else:
        while pau > 1:
            mos = 0
            while mos < pau:
                if my_list[mos] > my_list[mos + 1]:
                    temp = my_list[mos]
                    my_list[mos] = my_list[mos + 1]
                    my_list[mos + 1] = temp
                mos += 1
            pau -= 1
    return my_list[x]
