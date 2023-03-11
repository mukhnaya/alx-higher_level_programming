#!/usr/bin/python3
def no_c(my_string):
    '''
    convert my_string to a list
    remove characters and then
    reconvert back to a string
    '''
    mos = len(my_string)
    my_string_lis = []
    for pau in range(mos):
        my_string_lis.append(my_string[pau])
    list1 = []
    for elem in my_string_lis:
        if elem != 'c' and elem != 'C':
            list1.append(elem)
    new_string = ""
    for x in list1:
        new_string = new_string + x
    return new_string
print(no_c("Best School"))
print(no_c("Chicago"))
